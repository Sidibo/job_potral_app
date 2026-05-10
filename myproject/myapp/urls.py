from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('users/', views.users_list, name='users'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:id>/', views.edit_user, name='edit_user'),
    path('view-user/<int:id>/', views.view_user, name='view_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),

    path('jobs/', views.job_list, name='jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    path('applications/', views.applications_list, name='applications'),
    path('add-application/', views.add_application, name='add_application'),

    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('logout/', views.logout_view, name='logout'),

    path('add-job/', views.add_job, name='add_job'),
path('delete-job/<int:id>/', views.delete_job, name='delete_job'),

path('edit-job/<int:id>/', views.edit_job, name='edit_job'),
]