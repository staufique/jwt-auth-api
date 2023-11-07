from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
# Create your views here.

class StudentDetails(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            user = Student.objects.all()
            serializer = StudentSerializer(user, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif pk is not None:
            id = Student.objects.filter(pk=pk).first()
            serializer = StudentSerializer(id, data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'msg':'Not Found'},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        # user = request.data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"msg":"Data not Saved"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if pk is not None:
            id = Student.objects.filter(pk=pk).first()
            serializer = StudentSerializer(id, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg':'not found'},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        if pk is not None:
            id = Student.objects.filter(pk=pk).first()
            serializer = StudentSerializer(id, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg':'not found'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        if pk is not None:
            id = Student.objects.filter(pk=pk).first()
            id.delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_202_ACCEPTED)
        return Response({'msg':'not found'},status=status.HTTP_400_BAD_REQUEST)