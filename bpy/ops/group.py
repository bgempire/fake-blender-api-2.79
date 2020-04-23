import sys
import typing


def create(name: str = "Group"):
    '''Create an object group from selected objects 

    :param name: Name, Name of the new group 
    :type name: str
    '''

    pass


def objects_add_active(group: typing.Union[int, str] = ''):
    '''Add the object to an object group that contains the active object 

    :param group: Group, The group to add other selected objects to 
    :type group: typing.Union[int, str]
    '''

    pass


def objects_remove(group: typing.Union[int, str] = ''):
    '''Remove selected objects from a group 

    :param group: Group, The group to remove this object from 
    :type group: typing.Union[int, str]
    '''

    pass


def objects_remove_active(group: typing.Union[int, str] = ''):
    '''Remove the object from an object group that contains the active object 

    :param group: Group, The group to remove other selected objects from 
    :type group: typing.Union[int, str]
    '''

    pass


def objects_remove_all():
    '''Remove selected objects from all groups 

    '''

    pass
