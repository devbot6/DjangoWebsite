
from django.urls import path
from . import views
from views import *

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/add/', views.MemberAddView.as_view(), name='add'),
    path('members/edit/<int:id>', views.MemberEditView.as_view(), name='edit'),
    path('members/delete/<int:id>', deleteMember, name='delete'),
]
