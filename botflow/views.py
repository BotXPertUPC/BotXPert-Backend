from rest_framework import viewsets
from .models import BotFlow, Node, ListOption
from .serializers import BotFlowSerializer, NodeSerializer, ListOptionSerializer


class BotFlowViewSet(viewsets.ModelViewSet):
    queryset = BotFlow.objects.all()
    serializer_class = BotFlowSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class ListOptionViewSet(viewsets.ModelViewSet):
    queryset = ListOption.objects.all()
    serializer_class = ListOptionSerializer
