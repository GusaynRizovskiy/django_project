from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.request import Request
from myapiapp.serializers import GroupSerializer
from rest_framework.views import APIView
@api_view()
def hello_view(request: Request) -> Response:
    return  Response({"message": "Hellow World!"})

class GroupListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

