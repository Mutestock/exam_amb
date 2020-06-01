import click


@click.group()
def amb():
    pass


@amb.command()
@click.option("--path", "-p")
def add(path):
    if path:
        pass


@amb.command()
@click.option("--path", "-p")
def play(path):
    if path:
        pass
