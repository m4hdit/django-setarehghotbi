from django.urls import path
from .views import(
				SignUpView ,
				Activate ,
				LoginView ,
				LogoutView ,
				RestPasswordView ,
				RestPasswordActivate
			)

app_name='account'

urlpatterns=[
	path('signup/',SignUpView,name='sign_up'),
	path('activate/<slug:uidb64>/<slug:token>/', Activate, name='activate'),

	path('PasswrodActivate/<slug:uidb64>/<slug:token>/', RestPasswordActivate, name='rest_password_activate'),
	path('ResstPassword/',RestPasswordView,name='rest_password'),

	path('login/', LoginView, name='login'),
	path('logout/', LogoutView, name='logout'),
] 
