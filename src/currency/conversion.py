import requests
from fastapi import APIRouter, Request

from config.currency_api import curr_api
from src.currency.models import CurrencyParameter

router = APIRouter(
    tags=['Currency Conversion']

)


@router.get('/currency/')
async def currency_conversion(from_: str, to: str, amount: str):
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
        return {'Result': result, 'Status': status_code}
    except Exception as error:
        return {'error': str(error)}


@router.post('/api/v1/currency/')
async def currency_conversion(request: Request, currency: CurrencyParameter):
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
