
from sqlalchemy import create_engine, exists
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from model import Entry, base
from config import DevelopementConfiguration
from config.logger import logger
from schemas import *
import os


# Database configuration
class Database(DevelopementConfiguration):
    """_summary_

    Args:
        DevelopementConfiguration Herance: Herance from this class
    """


    def __init__(self) -> None:
        super().__init__()
        
        # Attributes
        self.database_needs_populate = False
        self.database_have_any_data = False
        
    
    def check_database_is_empty(self):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def get_frist_record(self, model: object):
        raise NotImplemented('Needs Implement in Derived Class')


    def get_last_entry(self):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def get_record(self, model: object, filter: str):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def record_exist(self, model: object, filter: str):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def get_last_record_date(self):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def have_any_record(self, model: object):
        raise NotImplemented('Needs Implement in Derived Class')


    def record_contain_string(self, contain_word: str, table_model: object):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def populate_database(self):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def get_all_data(self, table_model: object):
        return NotImplemented('Needs Implement in derived Class')
    
    
    def update_record(self, table_model: object, record: object):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def delete_record(self, table_model: object, record: object):
        raise NotImplemented('Needs Implement in Derived Class')
    
    
    def __str__(self) -> str:
        return f"""\n
        <------------- DATABASE DEBUG ------------->
        Database Needs Populate: {self.database_needs_populate}
        Database have any data: {self.database_have_any_data}
    
        """
        

class EntryDatabase(Database):
    """
        Entry Database management
        Derivate class from Database, to concentre management in Entry Database
    """

    
    def __init__(self):
        
        super().__init__()
        logger.debug('Entry Database Instanciate')
        
        # Frist create engine
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URI)

        if not os.path.exists(self.DB_PATH):
            os.makedirs(self.DB_PATH)

        # Check if database exist
        if not database_exists(self.engine.url):
            
            create_database(self.engine.url)
            self.database_needs_populate = True
            base.Base.metadata.create_all(self.engine) # Create Table

            
        # Create database session
        Session = sessionmaker(bind=self.engine) 
        self.session = Session()
        
        
        # Check if the database can received inital charge
        if self.database_needs_populate and self.INITAL_DATABASE_CHARGE:
            self.populate_database()
        

        self.database_have_any_data = self.have_any_record(Entry)
        
        
    def populate_database(self):
        
        """
            Make charge inital data if the database is new
        """
        
        for recordIndex in range(0, self.INITAL_DATA_TO_POPULATE_DATABASE + 1):
            
            # Generate temp entry ID linke DAY0001 to put in EntryID field in table
            temp_entry_id = self.PRE_FIX_TO_ID_GENERATE + str(recordIndex).zfill(self.DIGIT_TO_ID_GENERATE)
            
            record = Entry(
                entryID= temp_entry_id,
                title='Populate initial',
                content='Populate initial'
            )
            
            self.session.add(record)
            self.session.commit()

    
    def have_any_record(self, model: Entry):
        """
            If exist any record in database return True
        
        """
        #TODO essa função vai morrer depois que implementar outra para popular o banco
        result = self.session.query(exists().where(model.id != None)).scalar()
        
        if result:
            return True
        else:
            return False


    def get_last_entry(self) -> Entry:
        """
            Get Last record inserted in database
        """
        
        # If database have data
        if self.database_have_any_data:
            
            last_record = self.session.query(Entry).order_by(Entry.id.desc()).first()
            return last_record
        else:
            return database_empty_error()

    
    def get_record_by_field(self, field: str, valuer:str) -> Entry:
        """
            Get the frist occurrenc of record by field and valuer especific
        """
        
        query_result = self.session.query(Entry).filter(getattr(Entry, field) == valuer).first()
        
        if query_result:
            return query_result
        else:
            return record_not_found_error()
    

    def record_contain_string(self, contain_word: str, table_model: Entry, field: str):
        """
         If record cointain any character in parameter contain_word, return True
         
         @parameters:
            contain_word: Any string like search
            table_model: Object with the table model
            field: field in Table model to search data
        """
        
        try: # Trying make a query to search the word getattr(Entry, field)
            self.session.query(table_model).filter(
                                getattr(table_model, field).like(f'%{contain_word}%'))
            
            return True
        except MultipleResultsFound: # If found one o more return True
            return True
        
        except Exception as error: # Any another error return False
            return False
        
    
    def get_entry(self, entry_id: str) -> Entry:
        """Get entry in database and return it

        Args:
            entry_id (str): EntryID to search

        Returns:
            Entry: Try return the record entry in database
        """
        entry_data = self.session.query(Entry).filter(Entry.entryID == entry_id).first()
        
        if entry_data:
            return show_entry(entry_data), 200
        else:
            return {'message': 'Entry not found in database brow.'}, 404
        
    
    def get_next_entry_id(self):
        """
            Get new entry ID incremented
        """
        #FIXME não ta claro o retorno da função, se é um erro ou se é o PREFIX ID
        
        
        have_record_with_prefix = self.record_contain_string(self.PRE_FIX_TO_ID_GENERATE, Entry, 'entryID')
        
        print('Have any record with this prefix: ' + str(have_record_with_prefix))
        
        if self.database_have_any_data and have_record_with_prefix:
            
            query_result = self.get_last_entry()
            
            last_entry_id = query_result.entryID
            number_entry = last_entry_id.split(self.PRE_FIX_TO_ID_GENERATE)[1]
            new_increment_valuer = str(int(number_entry) + 1).zfill(len(number_entry))
            
            return self.PRE_FIX_TO_ID_GENERATE + new_increment_valuer
        
        elif not have_record_with_prefix: # If have data in database, but not exist an record with this PREFIX, so need create 
            return prefix_not_found_in_database()
        else:
            return record_not_found_error()
            
    
    def get_all_data(self):
        """Get all data in database
        """
        entrys = self.session.query(Entry).all()
        
        
        if entrys: # If exist products in database
            return get_all_entrys(entrys), 200
        else:
            return database_empty_error(), 404
        
    
    def delete_record(self, entry_id: str):
        
        result = self.session.query(Entry).filter(Entry.entryID == entry_id).delete()
        self.session.commit()
        
        if result:
            
            return {'mesage': f'Entry note {entry_id} has beem deleted from the base.'}, 200
        
        else:
            
            return {'mesage': 'Entry note not found in database'}, 404
    
    
    def update_record(self, new_title: str, new_content: str, entry_id: str) -> object:
        """Update Entry Record

        Args:
            new_title (str): new title for entry
            new_content (str): New content for entry
            entry_id (str): Entry id to make query

        Returns:
            _type_: Object
        """
        result = self.session.query(Entry).filter(Entry.entryID == entry_id).first()
        
        if result:
            
            result.title = new_title
            result.content = new_content
            self.session.commit()
            return {'mesage': f'Entry note {entry_id} update sucefull!'}, 200
        
        else:
            return {'mesage': 'Entry note not found in database'}, 404
        
                
        
    
    def __str__(self) -> str:
        return super().__str__()
