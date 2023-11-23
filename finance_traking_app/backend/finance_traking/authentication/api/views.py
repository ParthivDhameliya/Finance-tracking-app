from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from authentication.api.serializers import UserAccountSerializer
from authentication.models import UserAccount

User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error':'Email already exists.'})
            else:
                if len(password) < 8:
                    return Response({'error':'Passwrod must be atleast 8 characters long.'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({'success':'User created successfully.'})
        else:
            return Response({'error':'Passwords do not match.'})

class Accounts(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class AccountDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer