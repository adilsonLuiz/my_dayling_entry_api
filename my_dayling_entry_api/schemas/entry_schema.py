from pydantic import BaseModel
from typing import List, Optional
from model.entry import Entry
from config import APP_GLOBAL_CONFIG
from flask import jsonify





class EntrySchema(BaseModel):
    """
        Define how the new Entry to insert
        This can be used in parameter in main app.py to represent
        the parameters has expeted in function
    """
    entryID: str = APP_GLOBAL_CONFIG.ENTRY_ID_EXAMPLE
    title: str = 'Title dayling entry SCHEMA'
    content: str = 'My day today was realy cool SCHEMA'
    created: str = '1999-09-29 09:45:54.547831'


class GetNewIDToEntrySchema(BaseModel):
    """
        Difine how the ID to new Entry needs return
    
    """
    new_entry_id: str = APP_GLOBAL_CONFIG.ENTRY_ID_EXAMPLE


class ListingEntrysSchema(BaseModel):
    """Define How the Entrys needs show the data
    """

    entrys:List[EntrySchema]


class EntrySearchSchema(BaseModel):
    """Define how product is showing.
    """
    
    entryID: str = APP_GLOBAL_CONFIG.ENTRY_ID_EXAMPLE


class EntryDeleteSchema(BaseModel):
    """Define how the default response for delete entry
    """
    
    msg: str
    entryID: str


class EntryUpdateSchema(BaseModel):
    """Define how the default response for update entry
    """
    
    entryID: str
    mesage: str
    


def show_delete_operation(data_to_delete: str):
    """Return delete response

    Args:
        data_to_delete (str): name of data to presente in error message
        table_name (str): name of Table to presente in error message
    Returns:
        EntryDeleteSchema: Default Entry db schema
    """

    return {
        'msg': 'The record has been deleted succefull in database',
        'entryID': data_to_delete
    }, 200


def get_all_entrys(entrys: List[Entry]):
    """Return all entrys register in database.

    Args:
        entrys (List[Entry]): Query with all Data to return in response
    """
    
    result = []
    
    # For each entry, append the data and build the response
    for record in entrys:
        
        result.append({
            'entryID': record.entryID,
            'title': record.title,
            'content': record.content,
            'created': record.created,

        })

    return {'entrys': result}, 200


def show_entry(entry: Entry):
    """
        Show the entry information
    """
    
    return {
        'entryID': entry.entryID,
        'title': entry.title,
        'content': entry.content
    }, 200


def show_new_entry_id_prefix(new_id: str):
    """Return the new entryID response

    Args:
        new_id (str): new entryID to return

    Returns:
        _type_: _description_
    """
    return {
            'entryID': new_id
    }, 200