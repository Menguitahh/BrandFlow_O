from django.urls import path, include 
from rest_framework import routers
from BrandFlow_ import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router = routers.DefaultRouter()
router.register(r'User', views.UserSerializerView, basename='User')
router.register(r'Product', views.ProductSerializerView, basename='Product')
router.register(r'category', views.CategorySerializerView, basename='category')
router.register(r'Order', views.OrderSerializerView, basename='Order')
router.register(r'OrderDetails', views.OrderDetailsSerializerView, basename='OrderDetails')
# router.register(r'Payment', views.PaymentSerializerView, basename='Payment')
router.register(r'shoppcart', views.ShoppCartSerializerView, basename='shoppcart') 
router.register(r'shoppcartdetails', views.ShoppCartDetailsSerializerView, basename='shoppcartdetails') 
# router.register(r'method_payment', views.method_paymentSerializerView, basename='method_payment')
router.register(r'Reviews', views.ReviewsSerializerView, basename='Reviews')


urlpatterns = [
    path('BrandFlow_/model/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]