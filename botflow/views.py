from rest_framework import viewsets, generics
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

class NodesByBotFlowView(generics.ListAPIView):
    serializer_class = NodeSerializer

    def get_queryset(self):
        botflow_id = self.kwargs['botflow_id']
        return Node.objects.filter(bot_flow_id=botflow_id)