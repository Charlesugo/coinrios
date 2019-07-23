from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from login.views import administrator, registered_user, views


urlpatterns = [
    path('admin/', admin.site.urls),

    path("paystack", include(('paystack.urls', 'paystack'), namespace='paystack')),

    path('redirect/', views.redirect_base_on_role, name='redirect_base_on_role'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.CreateWhichUser.as_view(), name='select_user_to_create'),
    path('accounts/signup/admin/', administrator.AdministratorSignUpView.as_view(), name='create_admin'),
    path('accounts/signup/user/', registered_user.RegisteredUserSignUpView.as_view(), name='create_registered_user'),

    path('', include('crypto.urls')),
    path('registered-user/', include('registered_user.urls')),
    # path('', include('website.urls')),
    path('administrator/', include('administrator.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
