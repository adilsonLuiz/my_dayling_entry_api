# Interface CONFIG application Module


from config.global_config_app import GlobalApplicationConfigure, DevelopementConfiguration, HomologationConfiguration, ProductionConfiguration
from config.logger import logger


# Frist get global config to check enviroment running
GLOBAL_CONFIG = GlobalApplicationConfigure()



"""
This variables have any settings from database, like database name, path, configuration variables
from application, etc..
"""


if GLOBAL_CONFIG.ENVIROMENT == 'DEV':
    APP_GLOBAL_CONFIG = DevelopementConfiguration()
elif GLOBAL_CONFIG.ENVIROMENT == 'HM':
    APP_GLOBAL_CONFIG = HomologationConfiguration()
else:
    APP_GLOBAL_CONFIG = ProductionConfiguration()
    
    








