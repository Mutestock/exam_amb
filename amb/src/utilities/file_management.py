try:
    import six.moves.cPickle as pickle
except:
    import pickle
from pathlib import Path
from amb.definitions import TEMP_DIR


def picklify_object_list(data):
    if not (Path.is_dir(Path(TEMP_DIR))):
        Path.mkdir(Path(TEMP_DIR))
    output = open(f"{TEMP_DIR}/object_list_data.pkl", "wb")
    pickle.dump(data, output)


def retrieve_pkl_object_list():
    input = open(f"{TEMP_DIR}/object_list_data.pkl", "rb")
    data = pickle.load(input)
    return data


def clean_up_files():
    Path.unlink(Path(f"{TEMP_DIR}/object_list_data.pkl"))
    Path.rmdir(Path(TEMP_DIR))
