from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import BotFlow, Node, ListOption
from .serializers import BotFlowSerializer, NodeSerializer, ListOptionSerializer

@extend_schema(tags=["BotFlow"])
class BotFlowViewSet(viewsets.ModelViewSet):
    queryset = BotFlow.objects.all()
    serializer_class = BotFlowSerializer

@extend_schema(tags=["Nodes"])
class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

@extend_schema(tags=["ListOption"])
class ListOptionViewSet(viewsets.ModelViewSet):
    queryset = ListOption.objects.all()
    serializer_class = ListOptionSerializer

@extend_schema(tags=["Nodes"])
class NodesByBotFlowView(generics.ListAPIView):
    serializer_class = NodeSerializer

    def get_queryset(self):
        botflow_id = self.kwargs['botflow_id']
        return Node.objects.filter(bot_flow_id=botflow_id)

@extend_schema(
    tags=["BotFlow"],
    summary="Reemplazar los nodos de un botflow",
    description="Elimina todos los nodos de un botflow excepto el de tipo START y crea los nuevos nodos enviados (ignorando cualquier nodo START).",
    request=NodeSerializer(many=True),
    responses={201: NodeSerializer(many=True)}
)
class ReplaceBotFlowNodesView(APIView):
    def post(self, request, botflow_id):
        botflow = get_object_or_404(BotFlow, pk=botflow_id)
        data = request.data

        if not isinstance(data, list):
            return Response({'detail': 'Expected a list of nodes.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            start_node = botflow.start_node
            Node.objects.filter(bot_flow=botflow).exclude(id=start_node.id if start_node else None).delete()

            start_node_data = next((node for node in data if node.get('type') == 'START'), None)

            if start_node_data and start_node:
                next_node_id = start_node_data.get('next_node')
                if next_node_id is not None:
                    try:
                        # Nota: este nodo aún no existe, pero lo crearemos después
                        # así que solo guardamos el ID y lo resolveremos después
                        start_node.next_node_id = next_node_id
                        start_node.save()
                    except Exception:
                        pass  # podrías manejar errores aquí si el ID no es válido

            # Ignora los nodos de tipo START en la data
            filtered_data = [node for node in data if node.get('type') != 'START']

            # Crea los nuevos nodos (sin START)
            serializer = NodeSerializer(data=filtered_data, many=True)
            if serializer.is_valid():
                nodes = serializer.save(bot_flow=botflow)
                return Response(NodeSerializer(nodes, many=True).data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)