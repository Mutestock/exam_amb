import click
from amb.src.utilities.file_management import add_to_database


@click.group()
def amb():
    pass


@amb.command()
def add():
    """[manually loads file into database and program audio folder. Uses prompts]
    """
    print("")
    print("You're attempting to add a track to the program directory")
    print("Only .ogg and .wav sound extensions are supported")
    print("")

    path = click.prompt("Insert full track path with extension...")

    if path.split(".")[1] == "ogg" or path.split(".")[1] == "wav":
        genre = click.prompt("Please define a genre for the track e.g. 'forest'")
        add_to_database(path, genre)

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
