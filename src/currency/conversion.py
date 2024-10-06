import requests
from fastapi import APIRouter

from config.currency_api import curr_api

router = APIRouter(
    tags=['Currency Conversion']

)


@router.get('/api/v1/currency/')
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
