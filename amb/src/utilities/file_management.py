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



#def link_track_params_to_directory(track):
#    _create_missing_genre_dirs(track)


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
                copyfile(str(old_path),str(path_audio))
            except Exception as err:
                print("Error when copying file: ")
                print(err)

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


