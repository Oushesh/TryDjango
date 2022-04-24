'''
The aim here is to create some
views in the url.
Input: rendered data into json data
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

'''
We have 4 types
of request: post,get,put
'''

'''
@api_view(["GET"])
def getData(request):
	person = {'name':'Dennis','age':28}
	return Response(person)
'''

@api_view(['GET'])
def getData(request):
	items = Item.objects.all()
	serializer = ItemSerializer(items,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
	serializer = ItemSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

