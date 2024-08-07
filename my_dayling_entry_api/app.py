
from flask import redirect
import signal

# Import instance of main database to make operations..
from database import ENTRY_DB_CONNECTION

# Import global configuration variable to help config and manipulate settings of the application
from config import APP_GLOBAL_CONFIG
from schemas import *
from model import Entry
from config.logger import logger
from flask_openapi3 import OpenAPI
from flask_cors import CORS




# Initilize API with the OpenAPI
app = OpenAPI(__name__, info=APP_GLOBAL_CONFIG.INFO_INFORMATION_API)


CORS(app) # Apply CORS settings in app.

# Sett debug application based on global settings
app.config['DEBUG'] = APP_GLOBAL_CONFIG.DEBUG


# Signals control application

def close_server_checkups(signal, frame):
    """ Interact with the CRTL + C Signal output from keyboard.
    """
    print('-----Thanks for test it -----')
    print('---Sorry for any problems and bugs :/')
    exit(0)

# Signal to CRTL + C exit the program
signal.signal(signal.SIGINT, close_server_checkups)

    
### APP ROUTES ###

@app.get('/', tags=[APP_GLOBAL_CONFIG.HOME_TAG])
def home():
    """
        Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
        
    return redirect('/openapi')


@app.post('/new_entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRYS_OPERATION],
          responses={'200':EntrySchema, '404': ErrorSchema}
        )
def new_entry(form: EntrySchema):
    """Add new Entry to database
    """
    
    #Build new product
    new_entry = Entry(
        entryID=form.entryID,
        title=form.title,
        content=form.content
        )

    result = ENTRY_DB_CONNECTION.insert_new_data(new_entry)
    
    return result


@app.get('/generate_new_entry_id', tags=[APP_GLOBAL_CONFIG.TAG_ENTRYS_OPERATION], 
          responses={'200': GetNewIDToEntrySchema, '400': ErrorSchema}
          )
def generate_new_entry_id():
    """Return new entryID genereted.

    Returns:
        str: Object
    """


    result = ENTRY_DB_CONNECTION.get_next_entry_id()

    return result
    


@app.get('/entrys', tags=[APP_GLOBAL_CONFIG.TAG_ENTRYS_OPERATION],
         responses={'200': ListingEntrysSchema, '404': ErrorSchema})
def get_all_entrys():
    """Get all entrys in database and return it
    """

    result = ENTRY_DB_CONNECTION.get_all_data()
    
    return result


@app.get('/entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRYS_OPERATION],
         responses={'200': EntrySearchSchema, '404': ErrorSchema})
def get_entry(query: EntrySearchSchema):
    """Get unique entryID in database

    Args:
        query (EntrySearchSchema): _description_

    Returns:
        _type_: _description_
    """
    
    entry_id = query.entryID
    
    
    # Get entry data
    result = ENTRY_DB_CONNECTION.get_entry(entry_id)
    
    return result
    
    
@app.delete('/entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRYS_OPERATION],
         responses={'200': EntryDeleteSchema, '404': DeleteErrorSchema})
def delete_entry(query: EntrySearchSchema):
    """Delete record in entry db

    Args:
        query (EntrySearchSchema): parameter query comming from client
    """
    result = ENTRY_DB_CONNECTION.delete_record(query.entryID)
    
    return result


@app.put('/entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRYS_OPERATION],
         responses={'200': EntryUpdateSchema, '404': ErrorSchema})
def update_entry(query: EntrySearchSchema, form:EntrySchema):
    """Updata Entry note with new informations

    Args:
        query (EntrySearchSchema): Comming To Client request
        form (EntrySchema): Comming to Client Request

    Returns:
        _type_: _description_
    """
    result = ENTRY_DB_CONNECTION.update_record(form.title, form.content, query.entryID)
    
    return result


@app.get('/about', tags=[APP_GLOBAL_CONFIG.TAG_ABOUT_APPLICATION],
         responses={'200': AboutInformationSchema, '404': ErrorSchema})
def get_about_information():
    """Get about information from application
    """
    
    return {
        'api_version': APP_GLOBAL_CONFIG.API_VERSION
    }, 200