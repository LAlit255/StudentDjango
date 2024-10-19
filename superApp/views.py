from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer

class StudentListView(APIView):
    def get(self,request):
        s=Student.objects.all()
        serializer=StudentSerializer(s,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status=400)
    

class StudentDetailView(APIView):
    def get(self,request,pk):
            s=Student.objects.get(pk=pk)
            serializer=StudentSerializer(s)
            return Response(serializer.data)
        
    def put(self,request,pk):
            s=Student.objects.get(pk=pk)
            serializer=StudentSerializer(s,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors , status=400)
        

    def delete(self,request,pk):
            s=Student.objects.get(pk=pk)
            s.delete()
            return Response(status=204)