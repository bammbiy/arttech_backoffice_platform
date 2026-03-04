from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("dashboard/", include("apps.dashboard.urls")),
    path("admin/", admin.site.urls),
    path("api/artworks/", include("apps.artworks.api_urls")),

    # 로그인/로그아웃
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("artworks/", include("apps.artworks.urls")),
]

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]