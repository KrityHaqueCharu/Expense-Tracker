from .import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('expense-create/<int:id>', views.expense_create, name='expense-create'),
    path('budget-create/<int:id>',views.budget_create,name='budget-create'),
    path('add_category',views.add_category,name='add_category'),
    path('update_category/<int:pk>/',views.update_category,name="update_category"),
    path('delete_category/<int:pk>/',views.delete_category,name="delete_category"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('login/', auth_views.LoginView.as_view(template_name='appname/signin.html',authentication_form=LoginForm),name='login'),
    path('signout/', views.signout, name='signout'),
    path('budget_view/<int:pk>', views.budget_view,name='budget_view'),
    path('history',views.history,name='history'),
]
