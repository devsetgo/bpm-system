# -*- coding: utf-8 -*-

from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from endpoints.admin import endpoints as admin_pages
from endpoints.configuration import endpoints as config_pages
from endpoints.dashboard import endpoints as dash_pages
from endpoints.health import endpoints as health_pages
from endpoints.htmx import endpoints as htmx_pages
from endpoints.main import endpoints as main_pages
from endpoints.notes import endpoints as note_pages
from endpoints.user import endpoints as user_pages
from endpoints.notifications import endpoints as notifications_pages

routes = [
    Route("/", main_pages.homepage, name="dashboard", methods=["GET", "POST"]),
    Route("/about", main_pages.about_page, methods=["GET"]),
    Route("/dashboard", dash_pages.dashboard, methods=["GET"]),
    Mount(
        "/admin",
        routes=[
            Route("/open", endpoint=admin_pages.admin_index, methods=["GET", "POST"]),
            Route(
                "/all", endpoint=admin_pages.admin_all_requests, methods=["GET", "POST"]
            ),
            Route(
                "/login-failures",
                endpoint=admin_pages.login_attempts_page,
                methods=["GET", "POST"],
            ),
            Route(
                "/review/{page}",
                endpoint=admin_pages.admin_review,
                methods=["GET", "POST"],
            ),
        ],
        name="user",
    ),
    Mount(
        "/notifications",
        routes=[
            Route(
                "/attempts",
                endpoint=notifications_pages.login_attempts,
                methods=["GET"],
            ),
            Route(
                "/reg-req",
                endpoint=notifications_pages.registration_requests,
                methods=["GET"],
            ),
        ],
    ),
    Mount(
        "/notes",
        routes=[
            Route("/index", endpoint=note_pages.notes_index, methods=["GET", "POST"]),
            Route("/new", endpoint=note_pages.notes_new, methods=["GET", "POST"]),
            Route("/direction", endpoint=note_pages.notes_direction, methods=["POST"]),
            Route(
                "/{note_id}",
                endpoint=note_pages.notes_id,
                methods=["GET", "POST", "PUT"],
            ),
        ],
        name="notes",
    ),
    Mount(
        "/configuration",
        routes=[
            Route(
                "/",
                endpoint=config_pages.index,
                methods=["GET", "POST", "PUT", "DELETE"],
            ),
            Route("/tag/new", endpoint=config_pages.tag_new, methods=["GET", "POST"]),
            Route("/tag/view", endpoint=config_pages.tag_view, methods=["GET"]),
            Route("/tag/edit", endpoint=config_pages.tag_edit, methods=["GET", "PUT"]),
        ],
        name="configuration",
    ),
    Mount(
        "/user",
        routes=[
            Route(
                "/forgot", endpoint=user_pages.forgot_password, methods=["GET", "POST"]
            ),
            Route("/login", endpoint=user_pages.login, methods=["GET", "POST"]),
            Route("/logout", endpoint=user_pages.logout, methods=["GET", "POST"]),
            Route(
                "/password-change",
                endpoint=user_pages.password_change,
                methods=["GET", "POST"],
            ),
            Route("/profile", endpoint=user_pages.profile, methods=["GET"]),
            Route("/register", endpoint=user_pages.register, methods=["GET", "POST"]),
        ],
        name="user",
    ),
    Mount(
        "/htmx",
        routes=[
            Route(
                "/",
                endpoint=htmx_pages.index,
                methods=["GET", "POST", "PUT", "DELETE"],
            ),
            Route(
                "/user_search", endpoint=htmx_pages.user_search, methods=["GET", "POST"]
            ),
        ],
        name="htmx",
    ),
    Route("/health", endpoint=health_pages.health_status, methods=["GET"]),
    Mount("/static", app=StaticFiles(directory="statics"), name="static"),
]
