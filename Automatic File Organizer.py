from pathlib import Path
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}


def organize_files(folder):
    folder = Path(folder).expanduser().resolve()

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    for file in list(folder.iterdir()):
        if not file.is_file():
            continue

        destination = "Others"

        for category, extensions in CATEGORIES.items():
            if file.suffix.lower() in extensions:
                destination = category
                break

        target_dir = folder / destination
        target_dir.mkdir(exist_ok=True)

        target = target_dir / file.name

        if target.exists():
            print(f"Skipped existing file: {file.name}")
            continue

        shutil.move(str(file), str(target))
        print(f"Organized: {file.name} -> {destination}")


if __name__ == "__main__":
    path = input("Enter folder path to organize: ").strip()
    confirm = input(
        "This will move files. Continue? (yes/no): "
    ).lower()

    if confirm == "yes":
        organize_files(path)
    else:
        print("Operation cancelled.")
