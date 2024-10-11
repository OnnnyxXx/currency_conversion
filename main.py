from fastapi import FastAPI, Request, Form
from starlette.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from config.currency_api import curr_api
from src.currency.conversion import router as conversion_router
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title='Currency Conversion',

)

app.include_router(conversion_router)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    # port for react
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def currency_conversion(request: Request, from_: str = Form(...), to: str = Form(...), amount: str = Form(...)):
    """
    :param from_:
        This option is intended for the currency we are converting.

    :param to:
        This is the volute we are converting to.

    :param amount:
        Number of currencies convertible.

    :return:
        json response
    """
    try:
        url = f"https://api.apilayer.com/currency_data/convert?to={to}&from={from_}&amount={amount}"

        payload = {}
        headers = {
            "apikey": curr_api
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        print(result)

        return templates.TemplateResponse("index.html", {"request": request, "result": result, "status": status_code})
    except Exception as error:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(error)})
