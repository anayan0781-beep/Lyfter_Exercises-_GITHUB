import csv
from pathlib import Path


def get_video_games():
    video_games = []

    number_of_games = int(input("How many video games do you want to register? "))

    for i in range(number_of_games):
        print(f"\nVideo game #{i + 1}")

        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        esrb_rating = input("ESRB Rating: ")

        video_games.append([name, genre, developer, esrb_rating])

    return video_games


def save_video_games(video_games):
    folder = Path(__file__).resolve().parent
    file_path = folder / "video_games.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])
        writer.writerows(video_games)

    print(f"\nFile saved at: {file_path}")
    print("Video games saved successfully!")


def main():
    video_games = get_video_games()
    save_video_games(video_games)


if __name__ == "__main__":
    main()
