import pandas


def get_console_input():
    return input("Enter your data :")


def get_data_from_file(filename):
    file = open(filename, "r")
    read_content = file.read()
    return read_content


def get_data_pandas(filename):
    dataframe = pandas.read_csv(filename)
    return dataframe
