from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
	#widok posta
	path('', views.post_list, name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
		views.post.detail,
		name='post_detail')	
]