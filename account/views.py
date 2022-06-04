from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from account.models import User
from account.serializers import SignUpSerializer


class SignUpView(APIView):
    throttle_scope = "sendSMS"
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(
            email=serializer.validated_data['email'],
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            is_psycho=serializer.validated_data['is_psycho'],

        )
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(status=status.HTTP_201_CREATED)


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super(LogInSerializer, self).validate(attrs)
        # Custom data you want to include
        attrs.update({'id': self.user.id})
        return attrs


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer