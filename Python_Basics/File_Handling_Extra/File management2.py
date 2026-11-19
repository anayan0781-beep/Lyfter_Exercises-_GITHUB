
def process_file(input_filename, output_filename):
    """Read a file and save its content without line breaks."""
    with open(input_filename, "r", encoding="utf-8") as input_file:
        content = input_file.read()

    content = content.replace("\n", "").replace("\r", "")

    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write(content)

    print("File processed successfully!")


def main():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
