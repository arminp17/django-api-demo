from api.models import Appmodel
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Appmodel
from .serializers import AppmodelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated 



# Create your views here.

class AppmodelDetail(APIView):
    """
    Retrieve, update or delete a Appmodel instance.
    """
    # def get_object(self, pk):
    #     try:
    #         return Appmodel.objects.get(pk=pk)
    #     except Appmodel.DoesNotExist:
    #         raise Http404
    permission_classes = (IsAuthenticated, ) 
    # permission_classes = (AllowAny, ) 

    def get(self, request, format=None):
        Appmodelset = Appmodel.objects.all()
        serializer = AppmodelSerializer(Appmodelset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        for data in request.data:
            serializer = AppmodelSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     Appmodel = self.get_object(pk)
    #     Appmodel.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)