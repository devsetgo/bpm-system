# -*- coding: utf-8 -*-
"""
Application health endpoints
"""
import httpx
from loguru import logger
from pydantic.typing import resolve_annotations
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from core import login_required
from endpoints.workflow.form_processor import (
    process_form_variables,
    determine_form_type,
)

# page_url = "/workflow"
from resources import templates
from settings import config_settings

cam_auth = (
    config_settings.camunda_engine_user,
    config_settings.camunda_engine_password.get_secret_value(),
)
camunda_url = f"{config_settings.camunda_engine_url}/engine-rest"

section = "workflow"
page_url = f"/{section}"

client = httpx.AsyncClient()


@login_required.require_login
async def task_index(request):
    """
    Index page for notes
    """
    user_id = request.session["id"]
    user_name = request.session["user_name"]

    r = await client.get(f"{camunda_url}/task", auth=cam_auth)

    task_data = r.json()

    data: list = []
    for t in task_data:
        new_task = t
        sim_created = str(t["created"]).split("T")[0]
        new_task["sim_created"] = sim_created
        sim_due = str(t["due"]).split("T")[0]
        new_task["sim_due"] = sim_created
        sim_follow_up = str(t["followUp"]).split("T")[0]
        new_task["sim_follow_up"] = sim_created
        data.append(new_task)

    if r.status_code != 200:
        template = f"{page_url}/system.html"
        context = {
            "request": request,
            "active": "task-index",
            "section": section,
            "data": [],
        }
        logger.critical(context)
        logger.info("page accessed: /workflow/system")
        return templates.TemplateResponse(template, context)

    template = f"{page_url}/index.html"
    context = {
        "request": request,
        "active": "task-index",
        "section": section,
        "data": data,
    }
    logger.critical(context)
    logger.info("page accessed: /notes")
    return templates.TemplateResponse(template, context)


async def task_id(request):

    task_id = request.path_params["task_id"]
    r_task = await client.get(f"{camunda_url}/task/{task_id}", auth=cam_auth)
    task_data = r_task.json()
    form_type = await determine_form_type(task_data=task_data)

    # r_var = await client.get(f"{camunda_url}/task/{task_id}/variables", auth=cam_auth)
    # task_var = r_var.json()
    # task_form = {"form": task_form, "variables": task_var}
    # html_form = process_form_variables(html=task_form, variables=task_var)
    # print(html_form)
    template = f"{page_url}/task.html"
    context = {
        "request": request,
        "active": "task-index",
        "section": section,
        "task_data": task_data,
        "task_form": form_type,
        # "task_var": task_var,
        "task_id": task_id,
        "process_id": "X",
        "business_key": "X",
        "process_def": "X",
        # "html_form": html_form,
    }

    logger.critical(context)
    logger.info("page accessed: /notes")
    return templates.TemplateResponse(template, context)
