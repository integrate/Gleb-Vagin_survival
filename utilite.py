import os


def get_path(file):
    basa = os.path.split(__file__)[0]

    ways = file.split("/")

    return os.path.join(basa, *ways)
