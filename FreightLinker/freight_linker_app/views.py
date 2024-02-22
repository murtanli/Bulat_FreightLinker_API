from django.utils import formats
from django.http import FileResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class UserAuthenticationView(APIView):
    def post(self, request):
        data = request.data
        login = data.get('login')
        password = data.get('password')
        role = data.get('role')

        if login is None or password is None or role is None:
            return Response({'message': 'Логин, пароль и роль обязательны для аутентификации'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.get(login=login, password=password, role=role)
            return Response({'user_id': user.pk, 'message': 'Аутентификация успешна'}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'message': 'Неправильный логин, пароль или роль'})


class UserRegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            login = serializer.validated_data.get('login')
            password = serializer.validated_data.get('password')
            role = serializer.validated_data.get('role')

            # Проверяем, существует ли пользователь с таким логином
            existing_user = Users.objects.filter(login=login).first()
            if existing_user:
                return Response({'message': 'Пользователь с таким логином уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                # Создаем нового пользователя
                new_user = Users.objects.create(login=login, password=password, role=role)
                return Response({'user_id': new_user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class CreateTransport(APIView):
    def post(self, request):
        data = request.data
        serializer = TransportSerializer(data=data)
        if serializer.is_valid():
            # Сохраняем профиль транспорта
            transport = serializer.save()
            # Получаем ID созданного профиля
            transport_id = transport.id
            return Response({'transport_id': transport_id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class CreateDriverProfile(APIView):
    def post(self, request):
        data = request.data
        serializer = ProfileDriverSerializer(data=data)
        if serializer.is_valid():
            # Сохраняем профиль водителя
            profile_driver = serializer.save()
            # Получаем ID созданного профиля
            profile_id = profile_driver.id
            return Response({'profile_id': profile_id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class CreateUserProfile(APIView):
    def post(self, request):
        data = request.data
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            # Сохраняем профиль пользователя
            user_profile = serializer.save()
            # Получаем ID созданного профиля
            profile_id = user_profile.id
            return Response({'profile_id': profile_id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCargo(APIView):
    def post(self, request):
        data = request.data
        serializer = CargoSerializer(data=data)
        if serializer.is_valid():
            # Сохраняем груз
            cargo = serializer.save()
            return Response({'message': 'Груз успешно создан'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileTransport(APIView):
    def post(self, request):
        try:
            data = request.data['profile_id']
            profile = Profile_driver.objects.get(id=data)
            transports = Transport.objects.filter(profile_driver=profile)
            serializer_pr = ProfileDriverSerializer(profile)
            serializer = TransportSerializer(transports, many=True)
            return Response({'transport_inf': serializer.data, "profile_inf": serializer_pr.data}, status=status.HTTP_200_OK)
        except Profile_driver.DoesNotExist:
            return Response({"message": "Профиль не найден"}, status=status.HTTP_404_NOT_FOUND)

class CargoProfile(APIView):
    def post(self, request):
        profile_id = request.data.get('profile_id', None)
        if profile_id is not None:
            try:
                profile = User_Profile.objects.get(id=profile_id)
                cargos = Cargo.objects.filter(profile_id=profile)
                serializer_pr = UserProfileSerializer(profile)
                serializer = CargoSerializer(cargos, many=True)
                return Response({'cargo_inf': serializer.data, "profile_inf": serializer_pr.data}, status=status.HTTP_200_OK)
            except User_Profile.DoesNotExist:
                return Response({"message": "Профиль не найден"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Отсутствует параметр profile_id"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileDriver(APIView):
    def put(self, request):
        profile_id = request.data.get('profile_id')
        origin = request.data.get('origin')
        destination = request.data.get('destination')
        status_dr = request.data.get('status')

        if profile_id is not None:
            try:
                profile = Profile_driver.objects.get(id=profile_id)

                if origin is not None:
                    profile.origin = origin
                if destination is not None:
                    profile.destination = destination
                if status_dr is not None:
                    profile.status = status_dr

                profile.save()

                serializer = ProfileDriverSerializer(profile)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Profile_driver.DoesNotExist:
                return Response({"message": "Профиль не найден"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Отсутствует параметр profile_id"}, status=status.HTTP_400_BAD_REQUEST)


MONTHS_RU = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря',
}


class AllCargoes(APIView):
    def get(self, request):
        cargoes = Cargo.objects.all()
        serialized_cargoes = []

        for cargo in cargoes:
            cargo_data = CargoSerializer(cargo).data
            cargo_data['departure_time'] = cargo.departure_time.strftime('%d') + ' ' + MONTHS_RU[
                cargo.departure_time.month] + ' ' + cargo.departure_time.strftime('%Y')
            cargo_data['arrival_time'] = cargo.arrival_time.strftime('%d') + ' ' + MONTHS_RU[
                cargo.arrival_time.month] + ' ' + cargo.arrival_time.strftime('%Y')
            cargo_data['profile_info'] = {
                'fio': cargo.profile_id.fio,
                'number_phone': cargo.profile_id.number_phone,
            }
            serialized_cargoes.append(cargo_data)

        return Response(serialized_cargoes, status=status.HTTP_200_OK)