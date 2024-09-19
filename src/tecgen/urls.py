
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ImageUploadView

schema_view=get_schema_view(
    openapi.Info(
        title="Tecgen API",
        default_version='v1',
        description='Test Description',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='raselroky016@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include("user.urls")),
    path('catalog/',include('catalog.urls')),
    path('store/',include('store.urls')),
    path('campaign/',include('campaign.urls')),
    path('product/',include('product.urls')),
    path('configure/',include('configure.urls')),
    path('order/',include('order.urls')),
    path('stock/',include('stock.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('cart/',include('cartitem.urls')),
    # path('auth/', include('rest_authtoken.urls')),
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
    

    path('swagger',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),


] 


# urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)