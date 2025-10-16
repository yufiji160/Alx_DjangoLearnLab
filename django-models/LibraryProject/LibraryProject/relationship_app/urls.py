from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('', include('relationship_app.urls')),
]
