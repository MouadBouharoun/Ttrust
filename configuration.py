'''
Filename: configuration.py
Created: 2024-03-13
Author: Zakaria M

Summary:
[Provide a summary of the module's functionality. Highlight any key classes, or functions used.]
'''

from fastapi import APIRouter
from HBDS_TrustComputing.services.utils import get_logging, logger

# logger = get_logging()
# create router instance
config_router = APIRouter()

@config_router.get("/conf")
async def get_conf():
    logger.info("I'm config")
    return {"msg": "I'm config"}

@config_router.get("/auth")
async def get_auth():
    logger.info("I'm auth")
    return {"msg": "I'm auth"}