def output_to_console(text_to_out):
    """
    Function which makes output to console

    Args:
        text_to_out (str): Text to be displayed in console

    Returns:
        None. This function doesn't return any value.
    """
    print(text_to_out)


def output_to_file(filename):
    """
    Function which writes text to a file.

    Args:
        filename (str): The name of the file to write to.

    Returns:
        None. This function doesn't return any value.
    """
    try:
        with open(filename, 'w') as file2:
            file2.write('Hello world !!!')
    except Exception as e:
        print(f"Error: {e}")
