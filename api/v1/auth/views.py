from rest_framework.response import Response
import json
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.v1.auth.serializers import UserCreationSerializer
from authentication.models import User


@api_view(["POST"])
@permission_classes([AllowAny])
def createUserView(request):
    data = request.data
    username = request.data["username"]
    email = request.data["email"]
    password = request.data["password"]
    phone_number = request.data["phone_number"]
    place = request.data["place"]

    serializer = UserCreationSerializer(data=data)
    
    if serializer.is_valid():
        User.objects.create_user(
            username=username,
            email = email,
            password=password,
            phone_number = phone_number,
            place = place
            ) 

        # for login automatically after signup
        headers={
            "content-Type" : "application/json" 
        }
        data={
            "username" : username,
            "password" : password,
            "email" : email
        }

        protocol = "http://"
        if request.is_secure():
            protocol = "https://"
        host = request.get_host()

        url = protocol + host +"/api/v1/auth/token/"
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = {
            "status_code" : 6000,
            "data" : response.json(),
            "message" : "Account Created"
        }   
    else:
        response_data = {
            "status_code" : 6001,
            "message" : serializer.errors
        }    
    
    return Response(response_data)



