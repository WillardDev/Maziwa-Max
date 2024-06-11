import dataset as ds
import unittest


class TestDivideIntoBatches(unittest.TestCase):

    def test_divide_into_batches(self):
        # Test case 1: Divide by chunk size
        dataset_size = 1000
        chunk_size = 100
        expected_batches = [100] * 10

        actual_batches = ds.divide_into_batches(dataset_size, chunk_size)

        self.assertEqual(expected_batches, actual_batches)

        # Test case 2: Not divisible by chunk size
        dataset_size = 1234
        chunk_size = 256
        expected_inputs = [256, 256, 256, 124]

        actual_batches = ds.divide_into_batches(dataset_size, chunk_size)

        self.assertEqual(expected_inputs, actual_batches)

    if __name__ == "__main__":
        unittest.main()