from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



class LogView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({'data': 'GET'}, 200)

    def post(self, request):
        return Response({'data': 'POST'}, 200)