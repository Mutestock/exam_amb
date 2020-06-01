from gui.gui import guiApp
from amb.definitions import TEMP_DIR
from utilities.file_management import clean_up_files


if __name__ == "__main__":
    guiApp().run()
    clean_up_files()
