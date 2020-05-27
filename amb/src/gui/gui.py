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
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from amb.src.utilities.file_management import picklify

try:
    import six.moves.cPickle as pickle
except:
    import pickle


from amb.src.entities.track import Track


class ConfigurationPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")
    popup_name = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(ConfigurationPopup, self).__init__(**kwargs)
        self.obj = obj
        self.popup_name = Track.get_track_attribute_name_by_index(
            self.obj.index % Track.get_property_count()
        )
        self.obj_text = obj.text


class SelectableRecycleGridLayout(
    FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout
):
    pass
    """ Adds selection and focus behaviour to the view. """


class SelectableButton(RecycleDataViewBehavior, Button):
    """ Add selection support to the Button """

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
        if is_selected:
            print(rv.data[index])

    def on_press(self):
        if self.index % Track.get_property_count() == Track.get_property_count() - 1:
            # print(f"object variables: {self.index} {self.parent.parent.data[self.index+1-Track.get_property_count():self.index]}")
            pass
        elif not self.index % Track.get_property_count() == 0:
            popup = ConfigurationPopup(self)
            popup.open()

    def update_changes(self, txt):
        print()
        self.text = txt


class RV(BoxLayout):
    data_items = ListProperty([])
    track_object_size = 5

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_tracks()

    def get_tracks(self):
        track_list = []

        # Test data remove laster
        for _ in range(10):
            track_list.append(
                Track(
                    "wind",
                    "forest",
                    12,
                    {
                        "moneural": "Mono",
                        "interval": "Random 23 - 40",
                        "volume": "100% ",
                    },
                )
            )
            track_list.append(
                Track(
                    "river",
                    "forest",
                    9,
                    {"moneural": "Stereo", "interval": "Loop", "volume": "14-50% "},
                )
            )
            track_list.append(
                Track(
                    "Kazoo",
                    "annoying",
                    12,
                    {"moneural": "Mono", "interval": "Once", "volume": "3-50%"},
                )
            )

        for entry in track_list:
            self.data_items.append(entry.name)
            for value in entry.configuration.values():
                self.data_items.append(value)
        print(track_list)
        picklify(track_list)


class guiApp(App):
    title = "Ambience Player"

    def build(self):
        return RV()
