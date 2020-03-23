#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
# Mlist, 2020-Mar-21, Made a copy of this starter script
# Mlist, 2020-Mar-21, Added comments for existing __sort_tracks method to fully understand it
# Mlist, 2020-Mar-21, Modified CD class to include functionality requested in the TODOs
# Mlist, 2020-Mar-21, Build out Track class
# Mlist, 2020-Mar-21, Confirmed module is working by running TestHarness script
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    # -- Constructor -- #
    def __init__(self, position, title, length):
        """Set track position, track title and track length of a new Track Object"""
        #  --- Attributes -- #
        self.__position = position
        self.__title = title
        self.__length = length

    # -- Properties -- #

    # Track position
    @property
    def position (self):
        return self.__position
    @position.setter
    def position (self, value):
        self.__position = value

    # Track title
    @property
    def title (self):
        return self.__title
    @title.setter
    def title (self, value):
        self.__title = value

    # Track length
    @property
    def length (self):
        return self.__length
    @length.setter
    def length (self, value):
        self.__length = value

    # -- Methods -- #
    def __str__(self):
        """Returns Track details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.position, self.title, self.length)

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(self.position, self.title, self.length)

class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """


    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        """Set ID, Title, Artist and an empty list of tracks of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = [] #initiateing an empty tracklist for each CD object
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__tracks



    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """

        self.__tracks.append(track)
        self.__sort_tracks()# Re-sorting list after item has been added which creates and fills in potential blanks with None


    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """

        del self.__tracks[track_id - 1]
        self.__sort_tracks()# Re-sorting list after item has been removed which fills in removed blanks with None

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks) #assigning the number of tracks within a CD to a new variable
        for track in self.__tracks: # for each track stored in the track list of the CD object
            if (track is not None) and (n < track.position): # check if the track is already defined AND if the total number of tracks is smaller than the position ID of this track
                n = track.position #if this is true, which only happens when there are undefined gaps in the tracklist that have not been initiated: update the variable that store length of the track list with the max defined track index
        tmp_tracks = [None] * n  #creates a 'shell' list with the total number of tracks. each track is populated with 'None'
        for track in self.__tracks: #for each track listed in the actual track list of the CD object
            if track is not None: # if the track in the track list is already defined THEN
                tmp_tracks[track.position - 1] = track #override the empty shell track list where currently 'none' is listed with the actual track information. This sorts the list by referencing the track ID and using it as an index in the new, empty NONE list
        self.__tracks = tmp_tracks # overriding the actual track list of the CD object with the entered tracks PLUS empty, 'None' place holders

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result




