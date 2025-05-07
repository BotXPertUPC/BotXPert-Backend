from rest_framework import serializers
from .models import BotFlow, Node, ListOption


class ListOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOption
        fields = ['id', 'label', 'target_node', 'node']


class NodeSerializer(serializers.ModelSerializer):
    list_options = ListOptionSerializer(many=True, read_only=True)
    next_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all(), allow_null=True, required=False)
    id = serializers.IntegerField(required=True)

    class Meta:
        model = Node
        fields = [
            'id', 'bot_flow', 'type', 'text', 'position_x', 'position_y',
            'list_header', 'next_node', 'list_options'
        ]
        extra_kwargs = {'bot_flow': {'required': False}}


class BotFlowSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    start_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all(), allow_null=True, required=False)

    class Meta:
        model = BotFlow
        fields = [
            'id', 'name', 'description', 'created_at', 'updated_at',
            'phone_number', 'start_node', 'nodes'
        ]
