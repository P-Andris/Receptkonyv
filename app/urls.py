from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('uj_recept/', views.ujRecept, name = 'uj-recept'),
    path('recept_torlese/<int:id>/', views.receptTorlese, name = 'recept-torlese'),

    path('frissites/<int:id>/', views.indexFrissites, name = 'index-frissites')
]
