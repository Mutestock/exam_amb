import click
from amb.src.audio_handling.audio_utilities import get_audio_length
from amb.src.entities.track import Track
from amb.src.entities.configuration import Configuration
from amb.src.facades.track_facade import create
from amb.src.utilities.file_management import is_file_in_audio_folder


@click.group()
def amb():
    pass


@amb.command()
def add():
    """[manually loads file into database and program audio folder. Uses prompts]
    """
    print("")
    print("You're attempting to add a track to the program directory")
    print("Know that only .ogg and .wav sound formats are supported")
    print("")

    path = click.prompt("Insert full track path with extension...")

    if path.split(".")[1] == "ogg" or path.split(".")[1] == "wav":
        genre = click.prompt("Please define a genre for the track e.g. 'forest'")

        split = path.split("\\")[-1]
        split = split.split(".")

        name = split[0]
        extension = split[1]
        duration = get_audio_length(path)
        
        c = Configuration()
        t = Track(name, genre, duration, c, extension=extension)

        is_file_in_audio_folder(path,t)

        print("adding track to database ...")

        c.associate_database_variables()
        create(c)
        
        t.associate_database_variables()
        create(t)

        print("\nOK")

    else:
        print("Something went wrong with the input. Please check the extension")
        raise ValueError


@amb.command()
@click.option("--asdf", "-a")
def thing(asdf):
    if asdf:
        print("cake")
    else:
        print("wat")


@amb.command()
@click.option("--name", "-n")
def play(name):
    """[Manually play a file. Assumes that the file has been added to the database]

    :param name: [Track file name]
    :type name: [str]
    """
    if path:
        pass


if __name__ == "__main__":
    amb()
