import click


@click.group()
def amb():
    pass


@amb.command()
@click.option("--path", "-p", nargs=1)
def add(path):
    """[manually loads file into database and program audio folder]

    :param path: [path to file]
    :type path: [String]
    """
    print("????")
    if path:
        print("########")
        print(path)
        print(f"File extension = {path.split('.')}")
        print(f"File extension = {path.split('.')[1]}")
        print("########")
        #try:
        #    if path.split(".")[1] == ".ogg" or path.split(".")[1] == ".wav":
        #        print(f"Track successfully recognized on path: {path} ")
        #        genre = click.prompt('Which genre would you classify this as (Example: Forest)')
        #        print(f"You chose: {genre}")
        #    else:
        #        print(path)
        #        print(path.split('.')[0])
        #        err_msg = f"This program only supports files of the extensions: '.ogg', '.wav'. The inserted file had the extension {path.split(".")}"
        #        raise ValueError(err_msg)
        #except Exception as err:
        #    print(err)

@amb.command()
@click.option("--asdf",'-a')
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