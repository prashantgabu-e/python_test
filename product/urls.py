from django.urls import path, include
from rest_framework.routers import SimpleRouter

from product.views import ProductModelViewSet

router = SimpleRouter()
router.register("product", ProductModelViewSet, basename="product")

urlpatterns = router.urls
