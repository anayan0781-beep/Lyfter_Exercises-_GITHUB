import csv


def save_video_games():
    quantity = int(input("How many video games do you want to enter? "))

    with open("video_games_tabs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")

        writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])

        for i in range(quantity):
            print(f"\nVideo game {i + 1}")

            name = input("Enter the name: ")
            genre = input("Enter the genre: ")
            developer = input("Enter the developer: ")
            rating = input("Enter the ESRB rating: ")

            writer.writerow([name, genre, developer, rating])

    print("\nVideo games saved successfully!")


def main():
    save_video_games()


if __name__ == "__main__":
    main()
