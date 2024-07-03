from pydantic import BaseModel



class ErrorSchema(BaseModel):
    """Define how the error mesage is represent
    """
    error: str
    msg: str


class DeleteErrorSchema(BaseModel):
    """Define how the error delete needs presented
    """
    error: str = 'Error when trying delete this data.'
    record: str = 'record_error_to_delete'
    table: str = 'table name'
    

def delete_error(data_to_delete: str, table_name: str):
    """Return error to delete any data in table

    Args:
        data_to_delete (str): name of data to presente in error message
        table_name (str): name of Table to presente in error message
    Returns:
        DeleteErrorSchema: Error Schema
    """

    return {
        'error': 'Record is not found in database to delete, check the data has beem send.',
        'record': data_to_delete,
        'table': table_name
    }, 404


def database_empty_error():
    """Return error about not data in database

    Returns:
        ErrorSchema: Error schema
    """
    
    return {
        'error': 'The database is Empyt!',
        'msg': 'Try insert any data in database before.'
    }, 404
    

def record_not_found_error():
    """Return record not found error

    Returns:
        ErrorSchema: Error schema
    """
    
    return {
        'error': 'The Record is not found in the database',
        'msg': 'Check the data has beem send in request.'
    }, 404


def prefix_not_found_in_database():
    """Return PREFIX not found in database error

    Returns:
        ErrorSchema: Error schema
    """
    
    return {
        'error': 'This PREFIX dont exist in the database!',
        'msg': 'Try insert new record with this PREFIX in database, before make operations.'
    }, 404