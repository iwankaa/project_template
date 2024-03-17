from app.io.input import get_console_input, get_data_from_file, get_data_pandas
from app.io.output import output_to_console, output_to_file


def main():
    data_from_console = get_console_input()
    print("Data from user: ", data_from_console)

    data_from_file = get_data_from_file("data/file_to_read")
    print("Data from file:", data_from_file)

    data_from_csv = get_data_pandas("data/csv_file_to_read.csv")
    print("Data from Pandas:")
    print(data_from_csv)

    with open("data/output.txt", "w") as output_file:
        output_file.write("Data from user: " + data_from_console + "\n")
        output_file.write("Data from file: " + data_from_file + "\n")
        output_file.write("Data from Pandas:\n")
        output_file.write(data_from_csv.to_string(index=False))


if __name__ == "__main__":
    main()
