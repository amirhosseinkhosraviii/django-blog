from django .urls import path
from . import views

app_name='portfolio'
urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    # path('test/',views.test_view, name='test'),
]
