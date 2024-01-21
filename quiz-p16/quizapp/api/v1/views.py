from rest_framework import filters
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import QuizTypeSerializer, QuestionSerializer, ResultSerializer
from quizapp.models import QuizType, Question, Result


@api_view(['GET'])
def hello_world(request):
    test = request.query_params.get('test')
    if test != 'Hallo':
        data = {'message': 'Data not found'}
        return Response(data=data, status=status.HTTP_200_OK)
    data = {'test': 'Hello world'}
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def quiz_types(request):
    if request.method == 'GET':
        quiz_type = QuizType.objects.all()
        serializer = QuizTypeSerializer(quiz_type, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = QuizTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def quiz_type_detail(request, pk):
    try:
        quiz_type = QuizType.objects.get(pk=pk)
    except QuizType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuizTypeSerializer(quiz_type)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = QuizTypeSerializer(quiz_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAlD_REQUEST)

    if request.method == 'DELETE':
        quiz_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class SerializerGet(APIView):
#     def get(self, request):
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True, context={'request': request})
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
# class QuestionListAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#
#
# class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name']
    filter_backends = [filters.OrderingFilter]
    search_fields = ['pk', 'name']

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     search = self.request.query_params.get('search')
    #     if search:
    #         qs = qs.filter(name=search)
    #     return qs



    @action(detail=False, methods=['get'])
    def results(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        results = Result.objects.filter(user=request.user)
        serializer = ResultSerializer(results, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
