import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=1)


@api_view(['GET'])
def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        result = []
        for key in redis_instance.scan_iter():
            result.append(json.loads(redis_instance.get(key)))
            count += 1
            # redis_instance.delete(key)
        # response = {
        #     'count': count,
        #     'msg': f"Found {count} items.",
        #     'items': items
        # }
        return Response(result, status=200)


@api_view(['GET'])
def manage_item(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs['key']:
            request_key = kwargs['key'].upper()
            kys = redis_instance.keys(f"*{request_key}*")
            ans = []
            for ky in kys:
                val = json.loads(redis_instance.get(ky))
                if val:
                    # response = {
                    #     'key': ky,
                    #     'value': val,
                    #     'msg': 'success'
                    # }
                    ans.append(val)
            response = dict()
            response['data'] = ans
            return Response(ans, status=200)