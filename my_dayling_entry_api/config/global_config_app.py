
from .db_config import GlobalDatabaseConfiguration,  GlobalEntryDatabaseConfiguration
from flask_openapi3 import Info, Tag




class GlobalApplicationConfigure(GlobalEntryDatabaseConfiguration):
    """
        Root class to organize all importantes settings, like tags to swagger docs, and
        anothers variables importantes to application can be add here..
        
        This class is derived from GlobalDatabaseConfiguration, so here, we have, application settings from database,
        and application settings from application mainlines operations
    """

    def __init__(self):
        
        super().__init__()
        # DEBUG CONFIGURATION
        self.DEBUG = True
        self.CONFIGURATION_ENVIROMENTE_NAME = 'Global Configuration'

        # API Configuration
        self.API_VERSION = '0.0.2'
        
        # Set enviroment of Flask application Running
        
        self.ENVIROMENT = 'DEV' # Chose theese DEV-> Develoment, HM -> Homologation, PROD -> Production


        # Swagger DOC Configuration TAGS
        self.HOME_TAG = Tag(name='Documentation', description='Basic functions')
        self.TAG_ADD_NEW_ENTRY = Tag(name='New Entry', description='Add new Dayling Entrys notes')
        self.TAG_GET_ID_TO_NEW_ENTRY = Tag(name='Get ID to new Entry', description='Get new ID to entry')
        self.TAG_GET_ENTRYS = Tag(name='Entrys data', description='Get All database entrys data')
        self.TAG_ENTRY_SEARCH = Tag(name='Get entry Note', description='Return data from one unique Entry')
        self.TAG_ENTRY_DELETE = Tag(name='Delete entry', description='Delete entry note from database')
        self.TAG_ENTRY_UPDATE = Tag(name='Update Entry Record', description='Update any entry Record')
        self.TAG_ABOUT_APPLICATION = Tag(name='about application', description='Describe about many informations')
        
        # Swagger DOC Configuration INFOS
        self.INFO_INFORMATION_API = Info(title='My Entry Dayling API', version=self.API_VERSION)
        
        
        # Application behavior
        
        self.AUTO_DELETE_DB_AFTER_CLOSE_FLASK = False
        
        
    def __str__(self) -> str:
        return f'''\nENVIROMENT NAME: {self.ENVIROMENT}
CONFIGURATION SET: {self.CONFIGURATION_ENVIROMENTE_NAME}
DEBUG IS ENABLE: {self.DEBUG}
                '''


class DevelopementConfiguration(GlobalApplicationConfigure):
    """Configuration Developement application ambient
    """
    def __init__(self):
        super().__init__()
        self.CONFIGURATION_ENVIROMENTE_NAME = 'Developement'
        self.DEBUG = True
        self.AUTO_DELETE_DB_AFTER_CLOSE_FLASK = True

    def __str__(self) -> str:
        return super().__str__()
    
    
class HomologationConfiguration(GlobalApplicationConfigure):
    """Configuration Homologation application ambient
    """
    def __init__(self):
        super().__init__()
        self.CONFIGURATION_ENVIROMENTE_NAME = 'Homologation'
        self.DEBUG = True
    
    def __str__(self) -> str:
        return super().__str__()
        
        
class ProductionConfiguration(GlobalApplicationConfigure):
    """Configuration Production application ambient
    """
    def __init__(self):
        super().__init__()
        self.CONFIGURATION_ENVIROMENTE_NAME = 'Production'
        self.DEBUG = False
    
    def __str__(self) -> str:
        return super().__str__()