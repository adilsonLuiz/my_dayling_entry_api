
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
        self.TAG_ENTRYS_OPERATION = Tag(name='Entry DB Operations', description='Insert, List, Search, Update and Delete Entrys Notes.')
        self.TAG_ABOUT_APPLICATION = Tag(name='Aditional Routes Application', description='Routes Additional to presente informations about this application')
        
        # Swagger DOC Configuration INFOS
        self.INFO_INFORMATION_API = Info(title='My Entry Dayling API', version=self.API_VERSION)
        
        
        # Application behavior
        
        self.AUTO_DELETE_DB_AFTER_CLOSE_FLASK = False
        self.LOG_ROOT_PATH = 'log/'
        
        
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