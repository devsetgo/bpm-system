# -*- coding: utf-8 -*-

import time
from datetime import datetime

from loguru import logger
from sqlalchemy import and_
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse

from core import login_required
from core.crud_ops import execute_one_db, fetch_all_db, fetch_one_db
from core.db_setup import notes, tags
from resources import templates


@login_required.require_login
async def index(request):

    template = f"htmx/index.html"
    context = {"request": request}
    logger.info(f"page accessed: /htmx/{template}")
    return templates.TemplateResponse(template, context)


@login_required.require_login
async def user_search(request):

    user_id = request.session["id"]
    if "search" in request.query_params:
        terms = request.query_params["search"]
    else:
        terms = None

    query = (
        notes.select()
        .where(notes.c.user_id == user_id)
        .where(notes.c.note.ilike(f"%{terms}%"))
        .limit(100)
        .order_by(notes.c.date_created.desc())
    )

    try:
        # query database
        results = await fetch_all_db(query=query)
    except Exception as e:
        logger.error(f"error: {e}")
        results = []

    template = f"htmx/note_data.html"
    context = {"request": request, "data": results}
    logger.info(f"page accessed: /htmx/{template}")
    # adding sleep time to give search indication
    # time.sleep(.5)
    return templates.TemplateResponse(template, context)


# get notes for user
async def search_notes(user_id: str, terms: str = None):

    query = (
        notes.select()
        .where(notes.c.user_id == user_id)
        .where(notes.c.note.ilike(f"%{terms}%"))
        .limit(100)
        .order_by(notes.c.date_created.desc())
    )

    try:
        # query database
        results = await fetch_all_db(query=query)
        return results
    except Exception as e:
        logger.error(f"error: {e}")
