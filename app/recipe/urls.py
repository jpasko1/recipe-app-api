"""
URL mappingss for the recipe app.
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

router.register('tags', views.TagViewSet)

app_name = 'recipe' # name used when doing reverse URL lookups

urlpatterns = [
    path('', include(router.urls)),
]


