from pydantic import BaseModel
from typing import List, Optional
from model.entry import Entry
from config import APP_GLOBAL_CONFIG
from flask import jsonify



class AboutInformationSchema(BaseModel):
    """define how about Information is defined
    """
    api_version: str = APP_GLOBAL_CONFIG.API_VERSION



class TimeZoneInformationByIP(BaseModel):
    """ Define how time zone information comming
    """

    time_zone: dict