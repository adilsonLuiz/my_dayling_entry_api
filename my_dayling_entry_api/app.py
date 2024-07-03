
from flask import redirect

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

    
### APP ROUTES ###

@app.get('/', tags=[APP_GLOBAL_CONFIG.HOME_TAG])
def home():
    """
        Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
        
    return redirect('/openapi')


@app.post('/new_entry', tags=[APP_GLOBAL_CONFIG.TAG_ADD_NEW_ENTRY],
          responses={'200':EntrySchema, '409': ErrorSchema, '400': ErrorSchema}
        )
def new_entry(form: EntrySchema):
    """Add new Entry to database
    """
    #TODO migrate the commit to function inside database class
    
    #Build new product
    new_entry = Entry(
        entryID=form.entryID,
        title=form.title,
        content=form.content
        )

    logger.debug(f'Adding new Entry to DB..')

    try: # Try conect with the database and insert new Entry

        ENTRY_DB_CONNECTION.session.add(new_entry)
        ENTRY_DB_CONNECTION.session.commit()
        logger.debug('New Entry add sucessfull!')
        # Call my schema to show the entry
        return show_entry(new_entry), 200

    except Exception as err:
            logger.warning(f'An error is occurrend durant insert..')
            return {'mesage': err}


@app.get('/generate_new_entry_id', tags=[APP_GLOBAL_CONFIG.TAG_GET_ID_TO_NEW_ENTRY], 
          responses={'200': GetNewIDToEntrySchema, '400': ErrorSchema}
          )
def generate_new_entry_id():
    """Return new entryID genereted.

    Returns:
        str: Object
    """
    #FIXME não consigo saber se o retorno é o conteudo 200 ou nao

    new_entry_id = ENTRY_DB_CONNECTION.get_next_entry_id()

    if new_entry_id:
        print('Retornando 200 generate new entry')
        return show_entry_id(new_entry_id)
    else:
        print('Retornando 400 generate new entry')
        return 'error', 400


@app.get('/entrys', tags=[APP_GLOBAL_CONFIG.TAG_GET_ENTRYS],
         responses={'200': ListingEntrysSchema, '404': ErrorSchema})
def get_all_entrys():
    """Get all entrys in database and return it
    """

    result = ENTRY_DB_CONNECTION.get_all_data()
    
    return result


@app.get('/entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRY_SEARCH],
         responses={'200': EntrySearchSchema, '404': ErrorSchema})
def get_entry(query: EntrySearchSchema):
    
    entry_id = query.entryID
    
    
    # Get entry data
    result = ENTRY_DB_CONNECTION.get_entry(entry_id)
    
    return result
    
    
@app.delete('/entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRY_DELETE],
         responses={'200': EntryDeleteSchema, '404': ErrorSchema})
def delete_entry(query: EntrySearchSchema):
    """Delete record in entry db

    Args:
        query (EntrySearchSchema): parameter query comming from client
    """
    result = ENTRY_DB_CONNECTION.delete_record(query.entryID)
    
    return result


@app.put('/entry', tags=[APP_GLOBAL_CONFIG.TAG_ENTRY_UPDATE],
         responses={'200': EntryUpdateSchema, '404': ErrorSchema})
def update_entry(query: EntrySearchSchema, form:EntrySchema):
    
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