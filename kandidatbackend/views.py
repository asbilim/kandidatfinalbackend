from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

class UserCreation(ModelViewSet):

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    #none sense
    def create(self,request):

        username = request.data['username']
        password = request.data['password']

        if username and password:

            user = get_user_model().objects.create(username=username, password=password)
            user.set_password(password)  #this line of code is to insure the password is saved 
            
            return Response(status=status.HTTP_201_CREATED,data={'status':'success','content':'user created successfully'})
        
        return Response(status=status.HTTP_400_BAD_REQUEST,data={'status':'error','content':'An error occurred while creating the user!'})
    

    def get_permissions(self):
        
        permissions = [IsAdminUser]

        if self.action == 'create':

            permissions = []

        return [permission() for permission in permissions]



