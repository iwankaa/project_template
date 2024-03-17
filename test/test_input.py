import unittest
import pandas
from app.io.input import get_data_from_file, get_data_pandas


class TestDataFunctions(unittest.TestCase):

    def test_get_data_from_file(self):
        filename = "test_data.txt"
        with open(filename, "w") as file:
            file.write("Test data")
        self.assertEqual(get_data_from_file(filename), "Test data")

        non_existent_file = "non_existent_file.txt"
        self.assertEqual(get_data_from_file(non_existent_file), "\nError. File not found")

    def test_get_data_pandas(self):
        filename = "test_data.csv"
        dataframe = pandas.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        dataframe.to_csv(filename, index=False)
        self.assertTrue(get_data_pandas(filename).equals(dataframe))

        non_existent_file = "non_existent_file.csv"
        self.assertEqual(get_data_pandas(non_existent_file), "\nError. File not found")

        empty_file = "empty_file.csv"
        open(empty_file, 'a').close()
        self.assertEqual(get_data_pandas(empty_file), "\nError. Empty data in file")


if __name__ == '__main__':
    unittest.main()
