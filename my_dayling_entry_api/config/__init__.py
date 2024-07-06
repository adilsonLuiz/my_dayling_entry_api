# Interface CONFIG application Module


from config.global_config_app import GlobalApplicationConfigure, DevelopementConfiguration, HomologationConfiguration, ProductionConfiguration



# Frist get global config to check enviroment running
GLOBAL_CONFIG = GlobalApplicationConfigure()



"""
This variables have any settings from database, like database name, path, configuration variables
from application, etc..

Based on enviroment, the application go to instance different class with different configuration to control the execution and functionalits.
"""

# Check the enviroment 

if GLOBAL_CONFIG.ENVIROMENT == 'DEV':
    APP_GLOBAL_CONFIG = DevelopementConfiguration()
elif GLOBAL_CONFIG.ENVIROMENT == 'HM':
    APP_GLOBAL_CONFIG = HomologationConfiguration()
else:
    APP_GLOBAL_CONFIG = ProductionConfiguration()
    
    








