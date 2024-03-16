def output_to_console(text_to_out):
    print(text_to_out)

def output_to_file(filename):
    with open(filename, 'w') as file2:
        file2.write('Programming is Fun.')