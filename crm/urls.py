from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.home, name="crm-home"),
    path("profile/<int:pk>/", views.profile, name="crm-profile"),
    path("target/<int:pk>/", views.targetform, name="crm-target"),
    path("update_target/<int:pk>/", views.update_target, name="crm-update-target"),

    path("customer/", views.customer, name="crm-customer"),
    path("myadmin/", views.admin, name="crm-myadmin"),   

    path("register/", views.user_register, name="crm-user-register"),
    path("user_update/<int:pk>/", views.update_user, name="crm-user-update"),
    path("user_delete/<int:pk>/", views.delete_user, name="crm-user-delete"),

    path("logout/", LogoutView.as_view(template_name="crm/logout.html"), name="crm-logout"),    
    path("login/", LoginView.as_view(template_name="crm/login.html"), name="crm-login"),
    
    path("create_customer/", views.create_customer, name="crm-create-customer"),
    path("update_customer/<int:pk>/", views.update_customer, name="crm-update-customer"),
    path("delete_customer/<int:pk>/", views.delete_customer, name="crm-delete-customer"),

    path("detail/<int:pk>/", views.detail, name="crm-detail"),
    path("sales/<int:pk>/", views.sales, name="crm-sales"),
    path("update_sales/<int:pk>/", views.update_sales, name="crm-update-sales"),
    path("delete_sales/<int:pk>/", views.delete_sale, name="crm-delete-sales"),
    path("all_sales", views.all_sales, name="crm-all-sales"),

]