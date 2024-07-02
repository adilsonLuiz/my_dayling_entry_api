from pydantic import BaseModel



class ErrorSchema(BaseModel):
    """
        Define how the error mesage is represent
    """
    mesage: str
    solution: str


def database_empty_error():
    """General message error to not data found in database

    Returns:
        _type_: _description_
    """
    return {
        'mesage': 'The database is Empyt!',
        'solution': 'The database autopopulation control variable is disabled, and has no data for operation in EntryDB, try, \
        insert any data in database frist.'
    }, 404
    

def record_not_found_error():
    
    return {
        'mesage': 'The Record is not found in the database',
        'solution': 'This record dont exist, Please check the data being sent.'
    }, 404


def prefix_not_found_in_database_error():
    """General message error to not prefix found in database

    Returns:
        ErrorResponse 404: PREFIX NOT FOUND
    """
    return {'mesage': 
                'PREFIX not found in Entry Database',
                'solution': 'Try add new Entry ID with this PREFIX, and try again'
            }, 404