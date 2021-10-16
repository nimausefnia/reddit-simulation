from functools import partial
from rest_framework.response import Response
from .serializers import QuestionSerializer,AnswerSerializer
from .models import Question,Answer
from rest_framework import status
from rest_framework.views import APIView
from permissions import IsOwnerOrReadOnly
from rest_framework.permissions import  IsAuthenticated



class QuestionListView(APIView):
    def get(self,request,*args,**kwargs):
        question=Question.objects.all()
        ser_data=QuestionSerializer(instance=question, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)



class QuestionCreateView(APIView):  
     permission_classes=[IsAuthenticated,]
     def post(self,request,*args,**kwargs):
        ser_data=QuestionSerializer(data=request.data)
        if ser_data.is_valid() :
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
      
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)





class QuestionUpdateView(APIView):      
    permission_classes=[IsOwnerOrReadOnly,]
    def put(self,request,pk):
        question=Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        ser_data=QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)    



class QuestionDeleteView(APIView):        
    
    def delete(self,request,pk):
        question=Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        
        question.delete()
        return Response(status=status.HTTP_200_OK)        




class AnswerCreateView(APIView):  
     permission_classes=[IsAuthenticated,]
     def post(self,request,*args,**kwargs):
        ser_data=AnswerSerializer(data=request.data)
        if ser_data.is_valid() :
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
      
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

   



class AnswerUpdateView(APIView):      
    permission_classes=[IsOwnerOrReadOnly,]
    def put(self,request,pk):
        answer=Answer.objects.get(pk=pk)
        self.check_object_permissions(request,answer)
        ser_data=AnswerSerializer(instance=answer, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)    


class AnswerDeleteView(APIView):        
    
    def delete(self,request,pk):
        answer=Answer.objects.get(pk=pk)
        self.check_object_permissions(request,answer)
        
        answer.delete()
        return Response(status=status.HTTP_200_OK)            



        
