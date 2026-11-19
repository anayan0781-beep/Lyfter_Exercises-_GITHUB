def convert_to_uppercase(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as input_file:
        with open(output_filename, "w", encoding="utf-8") as output_file:
            for line in input_file:
                output_file.write(line.upper())


def main():
    convert_to_uppercase("input.txt", "output.txt")
    print("File converted successfully!")


if __name__ == "__main__":
    main()
    