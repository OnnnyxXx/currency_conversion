from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse

from src.currency.conversion import router as conversion_router
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title='Currency Conversion',

)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


app.include_router(conversion_router)
