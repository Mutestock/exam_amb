from amb.src.audio_handling.effect_controller import EffectController
from amb.src.facades.track_facade import *
from amb.src.connection.db_management import amb_engine

# Delete later
from amb.definitions import TEMP_DIR
from amb.src.entities.random_interval import RandomInterval
from amb.src.entities.track import Track
from amb.src.entities.configuration import Configuration
from amb.src.utilities.file_management import (
    retrieve_pkl_object_list,
    picklify_object_list,
    add_to_database as db_add,
)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    StringProperty,
    ObjectProperty,
)
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.config import Config

Config.set("graphics", "width", "1200")
Config.set("graphics", "height", "700")

import math

try:
    import six.moves.cPickle as pickle
except:
    import pickle

from pathlib import Path
import pygame


class ConfigurationPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")
    popup_name = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(ConfigurationPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text


class SelectableRecycleGridLayout(
    FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout
):
    pass
    """ Adds selection and focus behaviour to the view. """


class PlayAllButton(Button):
    color_on = [0, 1, 0, 1]
    color_off = [1, 0, 0, 1]

    def on_press(self):
        track_list = retrieve_pkl_object_list()
        ec = EffectController(track_list)
        ec.play_all()
        if self.background_color != self.color_on:
            self.background_color = self.color_on
        else:
            self.background_color = self.color_off


class StopAllButton(Button):
    def on_press(self):
        pygame.mixer.quit()


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class LoadFileButton(Button):
    def on_press(self):
        self.parent.show_load()


class GenrePopup(FloatLayout):
    text_input = ObjectProperty(None)


class ToolBar(GridLayout):
    file_path = StringProperty(None)
    genre = StringProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.file_path = str(filename[0])
        self.dismiss_popup()
        content = GenrePopup(text_input=self.get_genre)
        self._popup = Popup(title="Define genre", content=content, size_hint=(0.5, 0.3))
        self._popup.open()

    def get_genre(self, input):
        self.dismiss_popup()
        self.genre = input
        self.add_to_database()

    def add_to_database(self):
        db_add(str(Path(self.file_path)), self.genre)


class SelectableButton(RecycleDataViewBehavior, Button):
    """ Add selection support to the Button """

    track_object_size = 13
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        """ Add selection on touch down """
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        """ Respond to the selection of items in the view. """
        self.selected = is_selected
        # if is_selected:
        #    print(rv.data[index])

    def on_press(self):
        if self.index % self.track_object_size == self.track_object_size - 1:
            popup = ConfigurationPopup(self)
            popup.dismiss()
        elif not self.index % self.track_object_size == 0:
            popup = ConfigurationPopup(self)
            popup.open()

    def update_changes(self, txt):
        data = retrieve_pkl_object_list()
        track_object_size = len(data[0].__dict__.values()) + 1

        cell_nr = self.index
        # row_nr = math.floor((cell_nr + 1) / track_object_size)

        row_nr = math.floor(track_object_size / (cell_nr)) - 1
        print(track_object_size / (cell_nr))
        print(f"row: {row_nr}")
        local_cell = (cell_nr + 1) % track_object_size

        track = data[int(row_nr)]

        c = read(Configuration, Configuration.db_track_id, track.id)

        # to_update={
        #    1:track.db_name,
        #    2:track.db_genre,
        #    3:track.db_duration,
        #    4:c.db_mono_stereo,
        #    5:c.db_interval,
        #    6:c.db_volume,
        #    7:c.db_fade_beginning,
        #    8:c.db_fade_end,
        #    9:c.db_random_interval_max,
        #    10:c.db_random_interval_min,
        #    11:c.db_random_volume_max,
        #    12:c.db_random_volume_max,
        # }.get(local_cell)

        if local_cell == 4:
            c.db_mono_stereo = txt
        elif local_cell == 5:
            c.db_interval = txt
        elif local_cell == 6:
            c.db_volume = txt
        elif local_cell == 7:
            c.db_fade_beginning = txt
        elif local_cell == 8:
            c.db_fade_end = txt
        elif local_cell == 9:
            c.db_random_interval_max = txt
        elif local_cell == 10:
            c.db_random_interval_min = txt
        elif local_cell == 11:
            c.db_random_volume_max = txt
        elif local_cell == 12:
            c.db_random_volume_min = txt
        else:
            pass

        if local_cell > 3 and local_cell < 13:
            update(c)

        # to_change = list(track.configuration.__dict__.keys())[local_cell]
        # track.configuration[to_change] = txt

        picklify_object_list(data)

        data2 = refreshed_track_data()

        self.parent.parent.data = data2
        self.parent.parent.refresh_from_data(data2)


def refreshed_track_data():
    data = []
    for track in retrieve_pkl_object_list():
        c = read(Configuration, Configuration.db_track_id, track.id)
        data.append({"text": str(track.db_name)})
        data.append({"text": str(track.db_genre)})
        data.append({"text": str(track.db_duration)})
        data.append({"text": str(c.db_mono_stereo)})
        data.append({"text": str(c.db_interval)})
        data.append({"text": str(c.db_volume)})
        data.append({"text": str(c.db_fade_beginning)})
        data.append({"text": str(c.db_fade_end)})
        data.append({"text": str(c.db_random_interval_max)})
        data.append({"text": str(c.db_random_interval_min)})
        data.append({"text": str(c.db_random_volume_max)})
        data.append({"text": str(c.db_random_volume_min)})
        data.append({"text": "play"})
    return data


class RV(BoxLayout):
    data_items = ListProperty([])
    track_object_size = 13

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_tracks()

    def get_tracks(self):
        track_list = [track for track in read_all(Track)]
        for i, track in enumerate(track_list):
            track.channel = i * 2

        # Delete after db
        if not (Path.is_dir(Path(TEMP_DIR))):
            picklify_object_list(track_list)
        # decoded_list = retrieve_pkl_object_list()
        for track in track_list:
            c = read(Configuration, Configuration.db_track_id, track.id)
            self.data_items.append(track.db_name)
            self.data_items.append(track.db_genre)
            self.data_items.append(math.floor(track.db_duration * 100) / 100.0)
            self.data_items.append(c.db_mono_stereo)
            self.data_items.append(c.db_interval)
            self.data_items.append(c.db_volume)
            self.data_items.append(c.db_fade_beginning)
            self.data_items.append(c.db_fade_end)
            self.data_items.append(c.db_random_interval_max)
            self.data_items.append(c.db_random_interval_min)
            self.data_items.append(c.db_random_volume_max)
            self.data_items.append(c.db_random_volume_min)
            self.data_items.append("play")


class guiApp(App):
    title = "Ambience Player"

    def build(self):
        return RV()
