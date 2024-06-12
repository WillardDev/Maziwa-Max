import unittest
from unittest.mock import patch, MagicMock
import base_model as bm
import dataset as ds

class TestFineTuning(unittest.TestCase):
    @patch("builtins.print")
    @patch("base_model.Fine_Tune_adapter.fine_tune", return_value="mocked_metric")
    def test_fine_tuning(self, mock_fine_tune, mock_print):
        expected_batches = [
            (0, 100),  # Assuming each batch contains 100 samples
            (100, 200),
            # Add more batches as per your dataset
        ]

        num_epochs = 1
        count = 0

        with patch("builtins.print") as mock_print:
            while count < num_epochs:
                for batch_range in expected_batches:
                    start, end = batch_range
                    bm.Fine_Tune_adapter.fine_tune = MagicMock(return_value="mocked_metric")
                    bm.Fine_Tune_adapter.fine_tune(samples=ds.train_dataset[start:end])

                count += 1

        # Print the actual calls made to print
        print("Actual calls to print:")
        for call_args in mock_print.call_args_list:
            print(call_args)

if __name__ == '__main__':
    unittest.main()
