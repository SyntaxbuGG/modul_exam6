from django.urls import path
from .views import hello_world, quiz_types, quiz_type_detail
# from .views import  QuestionListAPIView, QuestionDetailAPIView
# from quizapp.api.v1 import views
from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()

router.register(r'questions', QuestionViewSet)




urlpatterns = [
    path('', hello_world),
    path('1/', quiz_types, name='quiz_types'),
    path('types/<int:pk>', quiz_type_detail),
    # path('serializer/', views.SerializerGet.as_view()),
    # path('question/', QuestionListAPIView.as_view(), name='question-listapi'),
    #1
    # path('question/<int:pk>/', QuestionDetailAPIView.as_view(), name='quest_detail')

]

urlpatterns = urlpatterns + router.urls