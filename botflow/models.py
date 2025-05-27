from django.core.exceptions import ValidationError
from django.db import models
# from django.contrib.auth.models import User

class BotFlow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bot_flows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_node = models.OneToOneField('Node', on_delete=models.SET_NULL, null=True, blank=True, related_name='starting_botflow')
    phone_number = models.CharField(max_length=20)

    def clean(self):
        if self.start_node and self.start_node.type != 'START':
            raise ValidationError('El nodo inicial (start_node) debe ser de tipo START.')

    def __str__(self):
        return self.name


class Node(models.Model):
    class NodeType(models.TextChoices):
        START = 'START', 'Start'
        TEXT = 'TEXT', 'Text'
        IMAGE = 'IMAGE', 'Image'
        FILE = 'FILE', 'File'
        ANSWER = 'ANSWER', 'Answer'
        LIST = 'LIST', 'List'
        END = 'END', 'End'

    id = models.IntegerField(primary_key=True)
    bot_flow = models.ForeignKey('BotFlow', on_delete=models.CASCADE, related_name='nodes')
    type = models.CharField(max_length=50, choices=NodeType.choices)
    text = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    file_url = models.URLField(blank=True, null=True)
    position_x = models.FloatField(null=True, blank=True)
    position_y = models.FloatField(null=True, blank=True)
    list_header = models.CharField(max_length=255, blank=True, null=True)
    next_node = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_nodes')

    def __str__(self):
        return f"{self.type} Node (ID: {self.id})"


class ListOption(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='list_options')
    label = models.CharField(max_length=255)
    target_node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True, blank=True, related_name='target_nodes')

    def clean(self):
        if self.node.type != 'LIST':
            raise ValidationError('El nodo (node) debe ser de tipo LIST.')