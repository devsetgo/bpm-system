# -*- coding: utf-8 -*-
"""
Application notifiactions endpoints
"""

from datetime import datetime, timedelta

from loguru import logger
from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse

from core.crud_ops import fetch_all_db
from core.db_setup import user_login_failures, user_approval

from resources import templates
from core import login_required


page_url = "/admin"


@login_required.require_login
async def login_attempts(request):
    """
    Attempted logins that have failed
    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    since_date = datetime.utcnow() - timedelta(days=30)
    query = user_login_failures.select().where(
        user_login_failures.c.date_created >= since_date
    )
    data = await fetch_all_db(query)
    logger.info(f"query login failures since {str(since_date)}")
    return HTMLResponse(f"{len(data)}")


@login_required.require_login
async def registration_requests(request):
    """
    Attempted logins that have failed
    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """

    query = (
        user_approval.select()
        .where(user_approval.c.is_reviewed == False)
        .order_by(user_approval.c.date_created.asc())
    )
    data = await fetch_all_db(query)

    print(data)
    logger.info(f"query awaiting registrations")
    return HTMLResponse(f"{len(data)}")
