from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Register
from .serializers import Registerserializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect
from rest_framework.generics import (CreateAPIView)

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = Register(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = Register()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def registerlist(request):
    if request.method == 'GET':
        register2 = Register.objects.all()
        serializer1=Registerserializers(register2,many=True)
        return JsonResponse (serializer1.data, safe = False)
    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer1=Registerserializers(data=data)

        if serializer1.is_valid():
            serializer1.save()
            return JsonResponse (serializer1.data, status = 201)
        return JsonResponse(serializer1.errors, status = 400) 

class ImageCreateAPIView(CreateAPIView):
	serializer_class = Registerserializers
	queryset = Register.objects.all()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



