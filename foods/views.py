from django.db.models import Prefetch
from rest_framework import generics, permissions

from .models import Food, FoodCategory
from .serializers import FoodListSerializer


class FoodsList(generics.ListAPIView):
    queryset = (
        FoodCategory.objects.prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))
        )
        .filter(food__is_publish=True)
        .distinct()
    )
    serializer_class = FoodListSerializer
    permission_classes = [permissions.IsAuthenticated]
