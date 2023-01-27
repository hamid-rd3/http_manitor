from django.urls import path
from .views import RegisterUserAPIView,AuthView
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi

schema_view = swagger_get_schema_view(
    openapi.Info(

        title="http manitor",
        default_version='1.0.0',
        description="send http requests and save the endpoints status  ",
        contact=openapi.Contact(
            email="h.dashtabadi@gmail.com"),
        terms_of_service="https://www.google.com/policies/terms/",

    ),
    public=True,
    # permission_classes=[permissions.AllowAny],

)
urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('api-register/', RegisterUserAPIView.as_view()),
    path('swagger-json/', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    
]
