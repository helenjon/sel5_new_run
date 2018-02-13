"""
Reads a settings file and writes its settings into a dictionary
:return: dictionary with settings
"""

def get_config():

    file_path = 'options.ini'
    settings = {}
    with open(file_path, 'r') as f:
        file_lines = f.read().split("\n")
        for line in file_lines:
            key = line.split("=")[0].strip()
            value = line.split("=")[1].strip()
            settings[key] = value
    return settings


