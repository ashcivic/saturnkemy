# accounts/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend.accounts import views as v
#from .views import EntregaList
from .views import EntregaViewSet

# Roteador do DRF
router = DefaultRouter()


# Rotas para APIs
#router.register(r'entregas', EntregaList, basename='entrega')
router.register(r'entregas', EntregaViewSet)
# Padrões de usuários
user_patterns = [
    path('', v.user_list, name='user_list'),
    path('create/', v.user_create, name='user_create'),
    path('<int:pk>/', v.user_detail, name='user_detail'),
    path('<int:pk>/update/', v.user_update, name='user_update'),
]

# URLs principais
urlpatterns = [
    path('login/', v.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', v.signup, name='signup'),
    path('reset/<uidb64>/<token>/', v.MyPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', v.MyPasswordResetComplete.as_view(), name='password_reset_complete'),
    path('password_reset/', v.MyPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', v.MyPasswordResetDone.as_view(), name='password_reset_done'),
    path('users/', include(user_patterns)),
    path('api/', include(router.urls)),  # Inclui todas as rotas do roteador
]

