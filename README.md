# MaziwaMax 🐄

**An AI-powered dairy farming assistant built with fine-tuned Llama2 and Retrieval-Augmented Generation (RAG)**

MaziwaMax is a specialized chatbot designed to help dairy farmers with farming-related questions, combining domain-specific fine-tuning with document retrieval for accurate, contextual responses.

## 🌟 Features

- **🤖 Fine-tuned AI Model**: Custom Llama2-13b model trained specifically for dairy farming
- **📚 RAG Pipeline**: Retrieval-Augmented Generation for context-aware responses
- **💬 Interactive Chat Interface**: Clean, user-friendly Streamlit web application
- **🔄 Conversation Memory**: Maintains context across conversation turns
- **📊 Model Evaluation**: Comprehensive testing with BLEU and ROUGE metrics
- **📱 Responsive Design**: Mobile-friendly interface with typing effects
- **🎯 Suggested Questions**: Pre-loaded questions to guide new users

## 🏗️ Architecture

```
MaziwaMax/
├── 📁 dataset/              # Training and knowledge base data
│   ├── 📁 json_files/       # Training datasets (JSON format)
│   ├── 📁 pdfs/            # PDF documents for knowledge base
│   └── 📁 text_files/      # Processed text files
├── 📁 style/               # CSS styling
├── 🐍 base_model.py        # Model configuration and setup
├── 🐍 fine_tune.py         # Model fine-tuning pipeline
├── 🐍 retrieval_augmented_generation.py  # RAG implementation
├── 🐍 user_interface.py    # Streamlit web interface
├── 🐍 model_evaluation.py  # Model performance evaluation
├── 🐍 model_inference.py   # Model inference utilities
└── 📁 tests/               # Unit tests
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Gradient AI account (for model fine-tuning)
- 8GB+ RAM recommended

### 1. Clone the Repository

```bash
git clone https://github.com/WillardDev/Maziwa-Max.git
cd Maziwa-Max
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv maziwamax_env

# Activate virtual environment
# On Windows:
maziwamax_env\Scripts\activate
# On macOS/Linux:
source maziwamax_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the project root:

```env
# Gradient AI Configuration
GRADIENT_ACCESS_TOKEN=your_gradient_access_token_here
GRADIENT_WORKSPACE_ID=your_workspace_id_here

# Optional: Other configurations
MODEL_MAX_TOKENS=128
TEMPERATURE=0.7
TOP_K=50
```

> **⚠️ Important**: Never commit your `.env` file to version control. Add it to `.gitignore`.

### 5. Prepare Dataset

Ensure your dataset files are in place:

```bash
# Your dataset structure should look like:
dataset/
├── json_files/
│   ├── dairy1.json
│   ├── dairy2.json
│   └── dairy3.json
├── text_files/
│   ├── dairy1.txt
│   ├── dairy2.txt
│   └── dairy3.txt
└── pdfs/
    ├── dairy1.pdf
    ├── dairy2.pdf
    └── dairy3.pdf
```

### 6. Run the Application

```bash
# Start the Streamlit web interface
streamlit run user_interface.py
```

The application will be available at `http://localhost:8501`

## 📋 Requirements

Create a `requirements.txt` file:

```txt
streamlit>=1.28.0
gradientai>=1.4.0
langchain>=0.0.340
langchain-community>=0.0.10
PyPDF2>=3.0.1
PyMuPDF>=1.23.0
nltk>=3.8.1
rouge>=1.0.1
haystack-ai>=2.0.0
gradient-haystack>=0.1.0
python-dotenv>=1.0.0
```

## 🔧 Configuration

### Model Configuration

Edit `base_model.py` to customize model settings:

```python
# Model hyperparameters
hyperparameters = {
    "epochs": 3,                    # Number of training epochs
    "batch_size": 100,             # Training batch size
    "learning_rate": 0.00005,      # Learning rate
    "rank": 8,                     # LoRA rank
    "temperature": 0.7,            # Response randomness
    "max_generated_token_count": 128  # Max response length
}
```

### RAG Configuration

Customize retrieval settings in `retrieval_augmented_generation.py`:

```python
# Document processing
chunk_size = 500                   # Text chunk size
embedding_model = "gradient"       # Embedding model
retrieval_top_k = 5               # Number of documents to retrieve
```

## 🎯 Usage Examples

### Basic Chat Interaction

```python
import retrieval_augmented_generation as rag

# Ask a question
question = "What are the best practices for dairy cow nutrition?"
response = rag.LLM_Run(question)
print(response)
```

### Fine-tuning the Model

```python
# Run fine-tuning
python fine_tune.py
```

### Evaluating Model Performance

```python
# Run evaluation metrics
python model_evaluation.py
```

### Converting PDFs to Text

```python
# Convert PDF documents to text format
python pdf_to_txt.py
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest

# Run specific test modules
python -m unittest model_evaluation_test.py
python -m unittest dataset_test.py
python -m unittest model_inference_test.py
```

## 📊 Model Evaluation

The project includes comprehensive evaluation metrics:

- **BLEU Score**: Measures translation quality
- **ROUGE Scores**: Evaluates summarization quality
- **Response Time**: Measures inference speed
- **User Satisfaction**: Tracks user feedback

View evaluation results:

```bash
python model_evaluation.py
```

## 🔄 Data Pipeline

### Adding New Documents

1. **PDF to Text Conversion**:
   ```bash
   python pdf_to_txt.py
   ```

2. **JSON Dataset Creation**:
   ```bash
   python json_editor.py
   ```

3. **Update RAG Knowledge Base**:
   - Place new text files in `dataset/text_files/`
   - Restart the application to reload documents

### Dataset Format

Training data should follow this JSON structure:

```json
[
    {
        "inputs": "<s>### Instruction:\nWhat are the signs of mastitis in dairy cows?\n\n### Response:\nMastitis in dairy cows can be identified by...</s>",
        "targets": "Response text here"
    }
]
```

## 🎨 Customization

### UI Styling

Modify `style/styles.css` to customize the interface:

```css
.chat-message.bot {
    background-color: #475063;  /* Bot message background */
}

.chat-message.user {
    background-color: #2b313e;  /* User message background */
}
```

### Suggested Questions

Edit `data/questions.txt` to modify suggested questions:

```txt
What are the best dairy cow breeds for tropical climates?
How can I improve milk production in my herd?
What vaccination schedule should I follow?
```

## 🚨 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Install missing dependencies
pip install -r requirements.txt
```

**2. API Authentication Errors**
```bash
# Check your .env file configuration
# Ensure GRADIENT_ACCESS_TOKEN and GRADIENT_WORKSPACE_ID are set
```

**3. Memory Issues**
```bash
# Reduce batch size in base_model.py
"batch_size": 50  # Instead of 100
```

**4. Streamlit Port Conflicts**
```bash
# Run on different port
streamlit run user_interface.py --server.port 8502
```

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance Optimization

### Model Optimization
- Adjust `max_generated_token_count` for faster responses
- Use quantization for memory efficiency
- Implement response caching for frequent questions

### RAG Optimization
- Optimize chunk sizes based on document types
- Use semantic chunking for better retrieval
- Implement document ranking algorithms

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run code formatting
black .
isort .

# Run linting
flake8 .
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Gradient AI** for the fine-tuning platform
- **Langchain** for the RAG framework
- **Streamlit** for the web interface
- **Haystack** for document processing
- **NousResearch** for the base Llama2 model

## 🗺️ Roadmap

- [ ] Multi-language support (Swahili, French)
- [ ] Mobile app development
- [ ] Image recognition for disease diagnosis
- [ ] Integration with weather APIs
- [ ] Offline mode support
- [ ] Voice input/output capabilities
- [ ] Advanced analytics dashboard

---

**Made with ❤️ for dairy farmers everywhere**
