import os
import shutil

def copy_pdfs(source_folder, destination_folder):
    # Traverse all subfolders and files in the source folder
    for root, _, files in os.walk(source_folder):
        for file in files:
            # Check if the file is a PDF file
            if file.endswith(".pdf"):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_folder, file)
                
                # Copy the PDF file to the destination folder
                shutil.copy(source_file_path, destination_file_path)
                print(f"Copying file: {file}")

if __name__ == "__main__":
    source_folder = "D:\\ZOTERO\\storage"  # Replace with your source folder path
    destination_folder = "E:\\pdf"  # Replace with your destination folder path

    # Ensure the destination folder exists; create it if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    copy_pdfs(source_folder, destination_folder)
    print("Copy completed")
