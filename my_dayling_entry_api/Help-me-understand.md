## ABOUT MODULES


### config dir - This module was designed to contain and concentrate all application settings
### database dir - This module was designed to contain configurations relevant to the database
### model dir - Standard module for application models
### schemas dir - Standard module for application schemas


## Behaviors you might like to try

# About DB operations
If you want to change any behavior related to the database, I recommend viewing the EntryDatabase class.
Now if you want to change characteristics of the database, I recommend the classes, GlobalEntryDatabaseConfiguration, GlobalDatabaseConfiguration


# About Application configuration
I decided to leave all the settings relevant to the application in separate classes. I think it's easier to have a place where we can concentrate all the settings and behaviors, so follow the tips below.

The GlobalApplicationConfigure class is the main API configuration class, and in it we set different behaviors and values. If you want to change something in the application settings globally, this could be a good way

My tip is not to touch the global class, but rather its derivatives, such as DevelopementConfiguration, here we can create specific attributes for the application development environment

the application automatically sets the environment, when the application is started in the init.py file of the configuration module, then you can take a look at it

# Add infos

Furthermore, the application was designed based on the future and scalability, which is why we decided to modularize configurations for expandability.
