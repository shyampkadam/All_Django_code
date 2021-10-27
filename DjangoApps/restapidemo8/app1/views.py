from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def handlingRequest1(request):
    return Response({'wish':'Welcome to API VIEW'})

@api_view(['GET'])
def handlingRequest2(request):
    return Response({'wish':'Welcome to API VIEW for GET Request'})

@api_view(['POST'])
def handlingRequest3(request):
    if request.method=="POST":
        #print(request.data)
        return Response({'wish':'Welcome to API VIEW for POST Request'})

@api_view(['GET'])
def handlingRequest2(request):
    return Response({'wish':'Welcome to API VIEW for GET Request'})

@api_view(['GET','POST'])
def handlingRequest4(request):
    if request.method == "GET":
        return Response({'msg':'This response is for GET Request'})
    if request.method=="POST":
        return Response({'msg':'This response is for POST Request'})