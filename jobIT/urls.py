from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'job_offerts', views.JobOffertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('job_offerts/<int:pk>', views.SingleJobOffertView.as_view(), name='job_offert'),
    path('job_offerts/city/<city>', views.CityView.as_view(), name='city'),
    path('job_offerts/service/<service>', views.ServiceView.as_view(), name='service'),

]
