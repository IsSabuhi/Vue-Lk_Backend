from fastapi import FastAPI
from config import envs
from routers.user_router import user_router

app = FastAPI(
    title=envs.TITLE_APP, version='v0.1',
    description=envs.DESCRIPTION_APP,
    docs_url=None, redoc_url=None
)

app.include_router(router=user_router)

# region SwaggerControllers
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


# endregion

if __name__ == '__main__':
    from uvicorn import run

    run('main:app', host=envs.HOST, port=envs.PORT, reload=True)
