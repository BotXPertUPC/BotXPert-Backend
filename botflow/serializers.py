from rest_framework import serializers
from .models import BotFlow, Node, ListOption


class ListOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOption
        fields = ['id', 'label', 'target_node', 'node']

    def validate(self, data):
        node = data.get('node')
        if node and node.type != Node.NodeType.LIST:
            raise serializers.ValidationError("The node must be of type LIST.")
        return data

class NodeSerializer(serializers.ModelSerializer):
    list_options = ListOptionSerializer(many=True, read_only=True)
    next_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all(), allow_null=True, required=False)
    id = serializers.IntegerField(required=True)

    class Meta:
        model = Node
        fields = [
            'id', 'bot_flow', 'type', 'text', 'image_url', 'file_url', 'position_x', 'position_y',
            'list_header', 'next_node', 'list_options',
        ]
        extra_kwargs = {'bot_flow': {'required': False}}

    def validate(self, data):
        node_type = data.get('type')
        image_url = data.get('image_url')
        file_url = data.get('file_url')
        list_header = data.get('list_header')
        text = data.get('text')
        next_node = data.get('next_node')

        if node_type == Node.NodeType.START:
            if text:
                raise serializers.ValidationError("A START node cannot have a text.")
            if image_url:
                raise serializers.ValidationError("A START node cannot have an image_url.")
            if file_url:
                raise serializers.ValidationError("A START node cannot have a file_url.")
            if list_header:
                raise serializers.ValidationError("A START node cannot have a list_header.")
        elif node_type == Node.NodeType.TEXT:
            if image_url:
                raise serializers.ValidationError("A TEXT node cannot have an image_url.")
            if file_url:
                raise serializers.ValidationError("A TEXT node cannot have a file_url.")
            if list_header:
                raise serializers.ValidationError("A TEXT node cannot have a list_header.")  
        elif node_type == Node.NodeType.IMAGE:
            if file_url:
                raise serializers.ValidationError("An IMAGE node cannot have a file_url.")
            if list_header:
                raise serializers.ValidationError("An IMAGE node cannot have a list_header.")
        elif node_type == Node.NodeType.FILE:
            if image_url:
                raise serializers.ValidationError("A FILE node cannot have an image_url.")
            if list_header:
                raise serializers.ValidationError("A FILE node cannot have a list_header.")
        elif node_type == Node.NodeType.ANSWER:
            if image_url:
                raise serializers.ValidationError("An ANSWER node cannot have an image_url.")
            if file_url:
                raise serializers.ValidationError("An ANSWER node cannot have a file_url.")
            if list_header:
                raise serializers.ValidationError("An ANSWER node cannot have a list_header.")
        elif node_type == Node.NodeType.END:
            if image_url:
                raise serializers.ValidationError("An END node cannot have an image_url.")
            if file_url:
                raise serializers.ValidationError("An END node cannot have a file_url.")
            if list_header:
                raise serializers.ValidationError("An END node cannot have a list_header.")
            if next_node:
                raise serializers.ValidationError("An END node cannot have a next_node.")

        return data

class BotFlowSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    start_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all(), allow_null=True, required=False)

    class Meta:
        model = BotFlow
        fields = [
            'id', 'name', 'description', 'created_at', 'updated_at',
            'phone_number', 'start_node', 'nodes'
        ]
