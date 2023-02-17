import fastapi
from fastapi.responses import HTMLResponse

from app.api.routers import main_router

app = fastapi.FastAPI()


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def read_root():
    return (
        '<h1>DOCS - <a href="http://127.0.0.1:8000/docs">'
        "http://127.0.0.1:8000/docs</a></h1>"
    )


app.include_router(main_router)
