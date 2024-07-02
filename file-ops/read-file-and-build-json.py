import os

current_folder = os.path.dirname(__file__)

# Construct the relative path to the file
file_path = os.path.join(current_folder, 'contacts.csv')


with open(file_path, 'r') as file:
    content = file.read()

json = {
    "file_content": content
}
print(json)
