from django.urls import path
from product.views import (
    CategoryApiView,
    CategorySingleApiView
    )


urlpatterns = [
    path('categories/', CategoryApiView.as_view(), name='categories'),
    path(
        'categories/<str:id>/',
        CategorySingleApiView.as_view(),
        name='category'
        )
]
