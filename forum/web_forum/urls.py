from django.urls import path
from web_forum.views.discus_view import DiscusListView, DiscusDetailView, DiscusUpdateView, DiscusCreateView, \
    AnswerCreateView, UserProfileDetailView, DiscusDeleteView, AnswerUpdateView, AnswerDeleteView

app_name = "web_forum"

urlpatterns = [
    path('', DiscusListView.as_view(), name="index"),
    path('discus/<int:pk>', DiscusDetailView.as_view(), name="discus_detail_view"),
    path('discus/add/', DiscusCreateView.as_view(), name="discus_add"),
    path('discus/<int:pk>/update', DiscusUpdateView.as_view(), name="discus_update_view"),
    path('discus/<int:pk>/delete', DiscusDeleteView.as_view(), name="discus_delete_view"),
    path('discus/<int:pk>/answers/add/', AnswerCreateView.as_view(), name="answer_add"),
    path('profile/', UserProfileDetailView.as_view(), name='user_profile'),
    path('answer/<int:pk>/update', AnswerUpdateView.as_view(), name="answer_update_view"),
    path('answer/<int:pk>/delete', AnswerDeleteView.as_view(), name="answer_delete_view"),
]
