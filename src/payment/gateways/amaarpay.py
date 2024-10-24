from typing import Dict
import logging
import json
from django.conf import settings
import requests
from user.models import User
logger = logging.getLogger('django')




def amarpay_payment_create(data: Dict, customer: User) -> Dict:
    """
    :param data:
    :param customer:
    :return:
    """
    customer_name = 'tecgen Customer'
    if customer.first_name and customer.last_name:
        customer_name = f'{customer.first_name} {customer.last_name}'
    try:
        body = {
            "store_id": settings.AMARPAY_LIVE_STORE_ID,
            "signature_key": settings.AMARPAY_LIVE_SIGNATURE_KEY,
            'currency': 'BDT',
            'desc': "not_available",
            'cus_name': customer_name,
            'cus_add1': customer.address if customer.address else 'Dhaka',
            'cus_add2': customer.address if customer.address else 'Dhaka',
            'cus_city': 'Dhaka',
            'cus_state': 'Dhaka',
            'cus_country': 'Bangladesh',
            'cus_phone': customer.username,
            'cus_email': customer.email if customer.email else 'info@shob.com.bd',
            'type': "json"
        }
        body.update(data)
        body = json.dumps(body)
        response = requests.post(
            url=settings.AMARPAY_LIVE_BASE_URL,
            data=body,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
        )
        resp: Dict = response.json()
        return resp

    except requests.exceptions.Timeout as e:
        logger.error('AmarPay_PAYMENT_TIMEOUT_ERROR: ', str(e))
    except requests.exceptions.HTTPError as e:
        logger.error('AmarPay_PAYMENT_HTTP_ERROR: ', str(e))
    except requests.exceptions.ConnectionError as e:
        logger.error('AmarPay_PAYMENT_CONNECTION_ERROR: ', str(e))
    except Exception as e:
        logger.error(f'Aamarpay error=>{e.__str__()}')
        print(e.__str__())
    return {}