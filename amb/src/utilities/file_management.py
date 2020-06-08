try:
    import six.moves.cPickle as pickle
except:
    import pickle
from pathlib import Path
from amb.definitions import TEMP_DIR
from amb.src.entities.track import Track
from pathlib import Path
from amb.definitions import AUDIO_DIR
from shutil import copyfile
from amb.src.audio_handling.audio_utilities import get_audio_length
from amb.src.entities.configuration import Configuration
from amb.src.facades.track_facade import create


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


def add_to_database(path, genre):

    split = path.split("\\")[-1]
    split = split.split(".")

    name = split[0]
    extension = split[1]
    duration = get_audio_length(path)

    c = Configuration()
    t = Track(name, genre, duration, c, extension=extension)
    is_file_in_audio_folder(path, t)

    print("adding track to database ...")

    c.associate_database_variables()
    create(c)

    t.associate_database_variables()
    create(t)

    print("\nOK")


def is_file_in_audio_folder(old_path, track):
    name = track.name
    genre = track.genre

    path_genre = Path(f"{AUDIO_DIR}/{genre}")
    path_audio = Path(f"{path_genre}/{track.name}.{track.extension}")

    if path_audio.is_file():
        print("file already exists in file system")
    else:
        if not path_genre.is_dir():
            print(f"{track.genre} was not a genre. Creating directory..")
            Path.mkdir(path_genre)
        print("copying file...")
        try:
            copyfile(str(old_path), str(path_audio))
        except Exception as err:
            print("Error when copying file: ")
            print(err)


# Possibly deprecated
def create_missing_genre_dirs(track):
    """[Audio subdirectories and the storage of the tracks, are categorized by their genre. This function generates missing directories, in case there is no directory representing the genre of a track]

    :param track: [Track object. Contains parametres like name, genre, configuration]
    :type track: [<class track.Track>]
    """
    genre_to_check = track.genre
    genre_path = Path(f"{AUDIO_DIR}/{genre_to_check}")
    if not genre_path.is_dir():
        print(f"{genre_path} was not a genre. Creating directory..")
        path.mkdir(genre_path)
