'''
serializers convert
object data types of json
files capable of being handled
by Django Rest API Framework
'''

from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'