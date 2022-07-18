from rest_framework.views       import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response    import Response

from drf_yasg.utils import swagger_auto_schema

class HelloApiView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(responses={200: 'Hello'})
    def get(self, request):
        message = 'Hello'
        return Response({'message': message}, status=200)