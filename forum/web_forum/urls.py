from django.urls import path

from web_forum.views.tasks_view import DiscusListView, DiscusDetailView, DiscusUpdateView
app_name = "web_forum"

urlpatterns = [
    path('', DiscusListView.as_view(), name="index"),
    path('projects/<int:pk>', DiscusDetailView.as_view(), name="discus_detail_view"),
    # path('discus/add/', ProjectCreateView.as_view(), name="project_add"),
    path('discus/<int:pk>/update', DiscusUpdateView.as_view(), name="discus_update_view"),
    # path('discus/<int:pk>/delete', ProjectDeleteView.as_view(), name="project_delete_view"),
    # path('discus/<int:pk>/answers/add/', TaskCreateView.as_view(), name="task_add"),
    # path('answers/<int:pk>', TaskDetailView.as_view(), name="task_view"),
    # path('answers/<int:pk>/update', TaskUpdateView.as_view(), name="task_update_view"),
    # path('answers/<int:pk>/delete', TaskDeleteView.as_view(), name="task_delete_view"),
    # path('discus/<int:pk>/add_user/', AddUserToProjectView.as_view(), name='add_user_to_project'),
    # path('discus/<int:pk>/remove_user/<int:user_pk>/', views.RemoveUserFromProjectView.as_view(),
    #      name='remove_user_from_project'),
]
