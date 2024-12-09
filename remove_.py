import os

def remove_(path):
    for root, dirs, files in os.walk(os.path.expanduser(path)):
        for file in files:
            if file.startswith('_'):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file[1:])
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_path} -> {new_file_path}")

remove_("~/.config/nvim/lua/plugins")
