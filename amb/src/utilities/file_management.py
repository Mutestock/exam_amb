try:
    import six.moves.cPickle as pickle
except:
    import pickle
from pathlib import Path
from amb.definitions import TEMP_DIR
from amb.src.entities.track import Track
from pathlib import Path
from amb.definitions import AUDIO_DIR


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


# Connect with database logic
def link_track_params_to_directory(track):
    _create_missing_genre_dirs(track)


def _create_missing_genre_dirs(track):
    """[Audio subdirectories and the storage of the tracks, are categorized by their genre. This function generates missing directories, in case there is no directory representing the genre of a track]

    :param track: [Track object. Contains parametres like name, genre, configuration]
    :type track: [<class track.Track>]
    """
    genre_to_check = track.genre
    genre_path = Path(f"{AUDIO_DIR}/{genre_to_check}")
    if not genre_path.is_dir():
        path.mkdir(genre_path)
