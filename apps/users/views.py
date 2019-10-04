from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import routers, serializers, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from apps.users.serializers import UserSerializers

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwarsg):
        serializer = self.serializer_class(data=request.data,
                                            context = {'resquest':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'is_superuser': user.is_superuser,
        }
        )
class UsersList(APIView):
    def get(self, request, format=None):
        rol = request.user.is_superuser
        if rol == True:
            queryset = User.objects.all()
            serializer = UserSerializers(queryset, many=True)        
            return Response(serializer.data)
        else:
            return Response("No eres administrador")

class UsersDetail(APIView):
    def get_object(self, id):        
        try:            
            return User.objects.get(pk=id) 
        except User.DoesNotExist: 
            return False
    
    
    def get(self, request, id, format=None):
        rol = request.user.is_superuser
        if rol == True:
            example = self.get_object(id)
            if example != False:
                serializer = UserSerializers(example)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            Response("No eres administrador")
    
    def put(self, request, id, format=None):        
        rol = request.user.is_superuser
        example = self.get_object(id)
        if rol == True:
            updateCajero = request.data
            #searchIdUser = User.objects.get(pk=id) 
            #serializerUser = UserSerializers(searchIdUser)
            #USER = serializerUser.data

            User.objects.filter(pk=id).update(
                is_superuser = updateCajero['is_superuser']
            )
            return Response("Ya eres adminisrador")
        else:
            return Response("No eres administrador")


