from gui.gui import guiApp
from pathlib import Path
from amb.definitions import TEMP_DIR

if __name__ == "__main__":
    guiApp().run()
    print(TEMP_DIR)
    Path.rmdir(Path(TEMP_DIR))
