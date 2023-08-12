from django.urls import path
from web_forum.views.tasks_view import DiscusListView, DiscusDetailView, DiscusUpdateView, DiscusCreateView, \
    AnswerCreateView, UserProfileDetailView

app_name = "web_forum"

urlpatterns = [
    path('', DiscusListView.as_view(), name="index"),
    path('discus/<int:pk>', DiscusDetailView.as_view(), name="discus_detail_view"),
    path('discus/add/', DiscusCreateView.as_view(), name="discus_add"),
    path('discus/<int:pk>/update', DiscusUpdateView.as_view(), name="discus_update_view"),
    # path('discus/<int:pk>/delete', ProjectDeleteView.as_view(), name="project_delete_view"),
    path('discus/<int:pk>/answers/add/', AnswerCreateView.as_view(), name="answer_add"),
    path('profile/', UserProfileDetailView.as_view(), name='user_profile'),
    # path('answers/<int:pk>', TaskDetailView.as_view(), name="task_view"),
    # path('answers/<int:pk>/update', TaskUpdateView.as_view(), name="task_update_view"),
    # path('answers/<int:pk>/delete', TaskDeleteView.as_view(), name="task_delete_view"),

]
