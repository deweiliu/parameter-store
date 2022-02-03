from os import listdir
from os.path import isfile, join, splitext


def get(dir):
    files = [f for f in listdir(dir) if isfile(join(dir, f))]

    paths = [join(dir, f) for f in files]
    app_names = [splitext(file)[0] for file in files]

    app_dict = {app_names[i]: paths[i] for i in range(len(app_names))}

    return app_dict
