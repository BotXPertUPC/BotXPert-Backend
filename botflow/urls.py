from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotFlowViewSet, NodeViewSet, ListOptionViewSet

router = DefaultRouter()
router.register(r'botflows', BotFlowViewSet)
router.register(r'nodes', NodeViewSet)
router.register(r'list-options', ListOptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
