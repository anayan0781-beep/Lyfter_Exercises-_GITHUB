from pathlib import Path


def read_songs(filename):
    folder = Path(__file__).parent
    file_path = folder / filename

    with open(file_path, "r", encoding="utf-8") as file:
        songs = [line.strip() for line in file.readlines()]

    return songs


def sort_songs(songs):
    songs.sort()
    return songs


def write_songs(filename, songs):
    folder = Path(__file__).parent
    file_path = folder / filename

    with open(file_path, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song + "\n")


def main():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    songs = read_songs(input_filename)
    sorted_songs = sort_songs(songs)
    write_songs(output_filename, sorted_songs)

    print("Songs sorted successfully!")


if __name__ == "__main__":
    main()