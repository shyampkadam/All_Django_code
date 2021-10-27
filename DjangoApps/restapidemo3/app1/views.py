from io import BytesIO

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from app1.serailizer import EmployeeSerializer

@csrf_exempt
def saveEmployee(request):
    if request.method=='POST':
        jsonData=request.body
        print(jsonData)
        jsonFormat=BytesIO(jsonData)
        #Now we have to convert json to model class  (Deserialization)
        pythonFormat=JSONParser().parse(jsonFormat)
        #Now we have to set pythonFormat data to Serializer
        serializedData=EmployeeSerializer(data=pythonFormat)
        if serializedData.is_valid():
            serializedData.save()
            responseToClient={'success':'Employee object is saved'}
            jsonData=JSONRenderer().render(responseToClient)
            return HttpResponse(jsonData,content_type='application/json')
        jsonData = JSONRenderer().render(serializedData.errors)
        return HttpResponse(jsonData, content_type='application/json')

