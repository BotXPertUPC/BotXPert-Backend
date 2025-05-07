from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotFlowViewSet, NodeViewSet, ListOptionViewSet, NodesByBotFlowView, ReplaceBotFlowNodesView

router = DefaultRouter()
router.register(r'botflows', BotFlowViewSet)
router.register(r'nodes', NodeViewSet)
router.register(r'list-options', ListOptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('botflows/<int:botflow_id>/nodes/', NodesByBotFlowView.as_view(), name='nodes-by-botflow'),
    path('botflows/<int:botflow_id>/nodes', ReplaceBotFlowNodesView.as_view(), name='replace-botflow-nodes'),
]
