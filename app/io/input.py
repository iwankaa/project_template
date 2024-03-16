import pandas


def get_console_input():
    """
    Function which gets data from user

    Returns:
        string: the data from user
    """
    return input("Enter your data :")


def get_data_from_file(filename):
    """
    Function which gets data from file

    Args:
        filename (str): The name of the file to  read.

    Returns:
        string: the data from file
    """
    file = open(filename, "r")
    read_content = file.read()
    return read_content


def get_data_pandas(filename):
    """
    Function that uses pandas to get data from file as a dataframe

    Args:
        filename (str): The name of the file to  read.

    Returns:
        string: the data from file as a dataframe
    """
    dataframe = pandas.read_csv(filename)
    return dataframe