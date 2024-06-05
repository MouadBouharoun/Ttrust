'''
Filename: router.py
Created: 2024-03-13
Author: Zakaria M

Summary:
This setup organizes the API endpoints into logical groups, making them easier to manage and document. Each router can handle specific types of requests.
'''

from fastapi import APIRouter
from .routes import computation, configuration

api_router = APIRouter()

# api_router.include_router(
#     configuration.config_router, tags=["configuration"], prefix="/param")

api_router.include_router(
    computation.computation_router, tags=["computation"], prefix="/Trust")