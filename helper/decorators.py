from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
import random

def identifier_builder(table_name: str, prefix: str = None) -> str:
    with connection.cursor() as cur:
        query = f'SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1;'
        cur.execute(query)
        row = cur.fetchone()
    try:
        seq_id = str(row[0] + 1)
    except:
        seq_id = "1"
    random_suffix = random.randint(10, 99)
    if not prefix:
        return seq_id.rjust(8, '0') + str(random_suffix)
    return prefix + seq_id.rjust(8, '0') + str(random_suffix)

def exception_handler(func):
    def inner_function(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except KeyError as ex:
            return Response({ex.__str__().strip("'"): ["This Field Is Required"]}, status=status.HTTP_400_BAD_REQUEST)
        except (ObjectDoesNotExist, Http404) as ex:
            return Response({'message': ex.__str__()}, status=status.HTTP_404_NOT_FOUND)
    return inner_function