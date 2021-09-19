# -*- coding: utf-8 -*-
"""
Application health endpoints
"""

from loguru import logger
from starlette.applications import Starlette
from starlette.responses import JSONResponse

# app = Starlette()

page_url = "/health"


async def health_status(request):
    """
    Application status endpoint with response of UP
    """
    logger.info(f"page {page_url}/status accessed")
    return JSONResponse({"status": "UP"})
