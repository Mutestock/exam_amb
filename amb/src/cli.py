import click


@click.group()
def amb():
    pass


@amb.command()
def add():
    """[manually loads file into database and program audio folder. Uses prompts]
    """
    print("####")
    print("You're attempting to add a track to the program directory")
    print("Know that only .ogg and .wav sound formats are supported")
    print("####")
    path = click.prompt("Insert full track path with extension...")
    print(path.split("."))
    print(path.split(".")[1])
    if path.split(".")[1] == "ogg" or path.split(".")[1] == "wav":
        genre = click.prompt("Please define a genre for the track e.g. 'forest'")
        print(f"{genre} was chosen.")
    else:
        print("Something went wrong with the input. Please check the extension")

        # try:
        #    if path.split(".")[1] == ".ogg" or path.split(".")[1] == ".wav":
        #        print(f"Track successfully recognized on path: {path} ")
        #        genre = click.prompt('Which genre would you classify this as (Example: Forest)')
        #        print(f"You chose: {genre}")
        #    else:
        #        print(path)
        #        print(path.split('.')[0])
        #        err_msg = f"This program only supports files of the extensions: '.ogg', '.wav'. The inserted file had the extension {path.split(".")}"
        #        raise ValueError(err_msg)
        # except Exception as err:
        #    print(err)


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
