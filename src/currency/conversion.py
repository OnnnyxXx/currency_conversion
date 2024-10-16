import requests
from fastapi import APIRouter, Request
from config.currency_api import curr_api
from src.currency.models import CurrencyParameter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=['Currency Conversion']

)


@router.post('/api/v1/currency/')
async def currency_conversion(request: Request, currency: CurrencyParameter):
    """
    This is an API for you, send json with parameters and get data with currency


    :param request:
        Well, it's all clear anyway

    :param currency:
        Pedantic model of checking data coming from the Frontend

    :return:
        Json object
    """
    try:
        url = f"https://api.apilayer.com/currency_data/convert"
        payload = {
            "to": currency.to,
            "from": currency.from_,
            "amount": currency.amount
        }
        headers = {
            "apikey": curr_api
        }
        response = requests.request("GET", url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.json()
        return {'Result': result, 'Status': status_code}
    except Exception as error:
        return {'error': str(error)}
