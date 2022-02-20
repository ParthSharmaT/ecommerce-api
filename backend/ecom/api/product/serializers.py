
from dataclasses import field
from email.mime import image
from importlib.metadata import requires
from unittest.util import _MAX_LENGTH
from urllib import request
from rest_framework import serializers
from .models import Product
class ProductSerializers(serializers.HyperlinkedModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
    class Meta:
        model=Product
        fields=('id','name','description','price','image','category')