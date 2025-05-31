from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.list_expenses, name='list_expenses'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('summary/', views.summary, name='summary'),
]