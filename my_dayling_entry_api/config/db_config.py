


class GlobalDatabaseConfiguration():
    """Application global Database configuration
    Here, we can have any attribute partinent to ALL database incomun settings, like debugs, inital populate..
    In General, configuration pertinent to ALL database in application and NOT one database specifyc.
    """
    
    
    def __init__(self) -> None:
        
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.ROOT_DB_PATH = 'db/'
        self.INITAL_DATA_TO_POPULATE_DATABASE = 20 # Valuer to populate DB with records automatic
        self.INITAL_DATABASE_CHARGE = True



class GlobalEntryDatabaseConfiguration(GlobalDatabaseConfiguration):
    """Classe to concentre configuration to Entry DB in application
    The Entry DB Is the main table in the application, so here we can sett, add and modify,
    configuration about this table, like name, path name ... field size and etc..
    """
    
    def __init__(self) -> None:
        
        super().__init__()
        self.ENTRY_TABEL_NAME = 'Entry'
        self.ENTRY_DB_NAME = 'entrys.db'
        self.DATABASE_ENTRY_URI  = f'sqlite:///{self.ROOT_DB_PATH}/{self.ENTRY_DB_NAME}'
        self.PRE_FIX_TO_ID_GENERATE = 'DAY' # PREFIX default of entrys id
        self.DIGIT_TO_ID_GENERATE = 5
        
        # Fields size entry db size
        self.FIELD_CONTENT_ENTRY_SIZE = 500
        self.FIELD_TITLE_SIZE = 100
        self.ENTRY_ID_EXAMPLE = self.PRE_FIX_TO_ID_GENERATE + ('0' * self.DIGIT_TO_ID_GENERATE) # Calculate total digits of PREFIX entry id

        # Calculating the Size dinamic based on prefix and digit total variables
        self.FIELD_ENTRY_ID_SIZE = int(len(self.PRE_FIX_TO_ID_GENERATE) + self.DIGIT_TO_ID_GENERATE)