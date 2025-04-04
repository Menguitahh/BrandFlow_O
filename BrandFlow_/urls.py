from django.urls import path, include 
from rest_framework import routers
from BrandFlow_ import views

router = routers.DefaultRouter()
# router.register(r'Category', views.CategoryView, basename='Category')
router.register(r'User', views.UserSerializerView, basename='User')
# router.register(r'Campaigns', views.CampaignView, basename='Campaigns')
# router.register(r'Orders', views.OrderView, basename='Orders')
# router.register(r'Campaignuser', views.CampaignUserSerializer, basename='Campaignuser')
urlpatterns = [
    path('BrandFlow_/model/', include(router.urls))
]