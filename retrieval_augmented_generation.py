from gradient_haystack.embedders.gradient_document_embedder import GradientDocumentEmbedder
from gradient_haystack.embedders.gradient_text_embedder import GradientTextEmbedder
from gradient_haystack.generator.base import GradientGenerator
from haystack import Document, Pipeline
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory.document_store import InMemoryDocumentStore
from haystack.components.retrievers.in_memory.embedding_retriever import InMemoryEmbeddingRetriever
from haystack.components.builders import PromptBuilder
from haystack.components.builders.answer_builder import AnswerBuilder
import os
import base_model as bm

class ConversationMemory:
    def __init__(self):
        self.conversation_history = []

    def add_to_memory(self, question, answer):
        self.conversation_history.append((question, answer))

    def get_memory(self):
        return self.conversation_history

# fine_tuned_Model_Id = "839aeb88-2008-47e6-9fb9-6ab8c11842d9_model_adapter"

document_store = InMemoryDocumentStore()
writer = DocumentWriter(document_store=document_store)

document_embedder = GradientDocumentEmbedder(
    access_token=bm.access_token,
    workspace_id=bm.workspace_id,
)

with open("./dataset/dairy3.txt", encoding="utf-8") as file:
    text_data = file.read()

docs = [
    Document(content=text_data)
]

indexing_pipeline = Pipeline()
indexing_pipeline.add_component(instance=document_embedder, name="document_embedder")
indexing_pipeline.add_component(instance=writer, name="writer")
indexing_pipeline.connect("document_embedder", "writer")
indexing_pipeline.run({"document_embedder": {"documents": docs}})

text_embedder = GradientTextEmbedder(
    access_token=bm.access_token,
    workspace_id=bm.workspace_id,
)

generator = GradientGenerator(
    access_token=bm.access_token,
    workspace_id=bm.workspace_id,
    model_adapter_id=bm.Fine_Tune_adapter.id
)

prompt = """You are helpful assistant ment to answer the questions relating to dairy farming only. Answer the query, based on the
content in the documents and don't let the user know that you are referring to a document. If you don't know the answer say you don't know. 
<<<<<<< HEAD
# Only answer questions related to the documents in your knowledge base. Don't let the user know you are using the documnets provided.
=======
# Only answer questions related to the documents in your knowledge base.
>>>>>>> 79a57e9dc8e9c1bce1c58f5fc273d8b7e20b133a
{{documents}}
Query: {{query}}
\nAnswer:"""

retriever = InMemoryEmbeddingRetriever(document_store=document_store)
prompt_builder = PromptBuilder(template=prompt)

rag_pipeline = Pipeline()
rag_pipeline.add_component(instance=text_embedder, name="text_embedder")
rag_pipeline.add_component(instance=retriever, name="retriever")
rag_pipeline.add_component(instance=prompt_builder, name="prompt_builder")
rag_pipeline.add_component(instance=generator, name="generator")
rag_pipeline.add_component(instance=AnswerBuilder(), name="answer_builder")
rag_pipeline.connect("generator.replies", "answer_builder.replies")
rag_pipeline.connect("retriever", "answer_builder.documents")
rag_pipeline.connect("text_embedder", "retriever")
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "generator")

def LLM_Run(question):
    result = rag_pipeline.run(
        {
            "text_embedder": {"text": question},
            "prompt_builder": {"query": question},
            "answer_builder": {"query": question}
        }
    )
    
    return result["answer_builder"]["answers"][0].data

# query = "What is the recommended breed to rear in Nyanza Province?"
# print(LLM_Run(query))

# conversation_memory = ConversationMemory()

# def LLM_Run(question):
#     # get the previous answers from the memory
#     conversation_history = conversation_memory.get_memory()

#     # Concatenate the conversation history and the new question
#     full_context = " ".join([q + " " + a for q, a in conversation_history] + [question])

#     # include the conversation history in the context for the model 
#     context = {
#         "text_embedder": {"text": full_context},
#         "prompt_builder": {"query": question},
#         "answer_builder": {"query": question}
#     }

#     result = rag_pipeline.run(context)

#     # add the new question and answer to the memory
#     answer = result["answer_builder"]["answers"][0].data
#     conversation_memory.add_to_memory(question, answer)

#     return answer

# query1 = "What are the characteristics of the Friesian breed?"
# query2 = "What of the Ayrshire breed?"
# query3 = "The characteristics"


# print(query1,"\n", LLM_Run(query1), "\n")
# print(query2,"\n", LLM_Run(query2), "\n")
# print(query3,"\n", LLM_Run(query3), "\n")
