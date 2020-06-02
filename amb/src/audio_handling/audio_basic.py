import multiprocessing as mp
from amb.definitions import AUDIO_DIR

# from track_configuration import modified_track_wav
from amb.src.entities.track import Track
import time
import random


class TrackRunner:
    def __init__(self, track_list):
        # self.__processing_tracks = track_list
        self.__track_list = track_list
        self.__processing_tracks = []
        for track in track_list:
            process = mp.Process(target=self.play_single, args=[track])
            self.__processing_tracks.append(process)

    def play_single(self, track):
        def play_track():
            print(f"Playing: {super.track.name}")

        process = mp.Process(target=play_track, args=[track])
        process.start()

    def _extract_from_numpy(self):
        raise NotImplementedError

    def play_all_alt(self):
        print(f"Length was: {len(self.__track_list)}")
        for track in self.__track_list:
            (lambda x: self.play_single(x))(track)

    def play_all(self):
        print(len(self.__processing_tracks))
        for process in self.__processing_tracks:
            process.start()

        for process in self.__processing_tracks:
            process.join()

    def stop_all(self):
        for process in self.__processing_tracks:
            print("Terminating all track processes...")
            process.terminate()
