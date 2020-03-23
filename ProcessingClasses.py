#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Mlist, 2020-Mar-21, Made a copy of this starter script
# Mlist, 2020-Mar-21, Build out methods and compared against example solution and run TestHarness.py
# Mlist, 2020-Mar-22, Added try/except in select_CD function in case provided ID is not an number
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        #A
        try:
            cd_idx = int(cd_idx)
        except ValueError:
            print('The entered value is not a number!')
            
        #Cycle through each CD object
        for CDobject in table:
            #check if the ID of the CD object is matching cd_idx
            if CDobject.cd_id == cd_idx:
                #if a match is found, return the CD object
                return CDobject
        raise Exception ('This ID does not exist')#if the entered ID does not find a match after each CD Object has been checked an exception will be raised

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: Raised in case position is not an integer.

        Returns:
            None:

        """

        position, title, length = track_info
        try:
            position = int(position)
        except Exception as e:
            raise Exception('Error adding track:\n' + str(e))
        track = DC.Track(position, title, length) #Initiates a new track object
        cd.add_track(track) #calls the add_track method in the CD class. This method appends the recieved track to the current CD object
        


