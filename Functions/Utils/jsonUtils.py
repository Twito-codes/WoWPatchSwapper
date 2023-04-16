import json


def load_data():
    with open("Data/Data.json", "r") as data_file:
        data = json.load(data_file)
    return data


def update_data(new_data):
    with open("Data/Data.json", "r") as data_file:
        data = json.load(data_file)
        data.update(new_data)
    with open("Data/Data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
