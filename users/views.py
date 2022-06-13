from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from common.utils import create_message
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from django.core.mail import send_mail
import string
import random


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        request.data['password'] = ''.join(random.choice(string.ascii_letters) for i in range(10))
        password = request.data['password']
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_mail(password, "Please use below password for login", "noreply@ropstorm.com", [request.data['email']],
                  fail_silently=False)
        return Response(create_message(False, 'success', [serializer.data]))


class LoginView(APIView):
    def post(self, request):
        email = request.data['username']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        data = {
            'jwt': token,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        response = Response(create_message(False, 'success', [data]))
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response