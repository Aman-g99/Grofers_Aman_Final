from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import *


class UpdateValueView(APIView):

    def post(self, request, *args, **kwargs):
        key = request.POST['key']
        value = request.POST['value']
        count = len(Store.objects.filter(key=key))
        if count:
            store = Store.objects.filter(key=key)[0]
            store.value = value
            store.save()
        else:
            store = Store(key=key, value=value)
            store.save()

        return Response(
            "success",
            status=status.HTTP_200_OK
        )


class GetValueView(APIView):

    def post(self, request, *args, **kwargs):
        key = request.POST['key']
        store = Store.objects.filter(key=key)
        count = len(store)
        if count:
            return Response(
                {'key': key, 'value': store[0].value},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                "error",
                status=status.HTTP_404_NOT_FOUND
            )


class WatchView(APIView):

    def post(self, request, *args, **kwargs):
        time = request.POST['time']
        store = Store.objects.filter(updated__gt=time).order_by('updated')
        count = len(store)
        dict=[]
        last = ""
        for i in range(count):
            dict.append({'key': store[i].key, 'value': store[i].value, 'updated': store[i].updated})
            last = store[i].updated
        if count:
            return Response(
                {'count': count, 'last': last, 'result': dict},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                "error",
                status=status.HTTP_404_NOT_FOUND
            )


class TimeView(APIView):

    def get(self, request, **kwargs):
        import datetime
        return Response(
            {'time': datetime.datetime.utcnow().isoformat()},
            status=status.HTTP_200_OK
        )
