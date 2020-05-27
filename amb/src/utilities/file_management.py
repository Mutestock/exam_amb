try:
    import six.moves.cPickle as pickle
except:
    import pickle
from pathlib import Path
from amb.definitions import TEMP_DIR


def picklify(data):
    print(TEMP_DIR)
    if not (Path.is_dir(Path(TEMP_DIR))):
        Path.mkdir(Path(TEMP_DIR))
    output = open(f"{TEMP_DIR}/object_list_data.pkl", "wb")
    pickle.dump(data, output)
