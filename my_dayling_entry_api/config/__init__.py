# Interface CONFIG application Module


from config.global_config_app import GlobalApplicationConfigure, DevelopementConfiguration
from config.logger import logger




#TODO Create logic to altern for production and Developement application
# Development Object


"""
This variables have any settings from database, like database name, path, configuration variables
from application, etc..
"""
APP_GLOBAL_CONFIG = DevelopementConfiguration()






