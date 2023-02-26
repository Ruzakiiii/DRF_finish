import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women



class Womenserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#
#         self.content = content


# def encod():
#     model = WomenModel('ALextiy', 'Joliii')
#
#     model_sr = Womenserializer(model)
#
#     print(model_sr.data, type(model_sr.data), sep='\n')
#
#     json = JSONRenderer().render(model_sr.data)
#
#     print(json)
#
# def decod():
#     stream = io.BytesIO(b'{"title":"ALextiy","content":"Joliii"}')
#
#     data = JSONParser().parse(stream)
#
#     serializer = Womenserializer(data=data)
#
#     serializer.is_valid()
#
#     print(serializer.validated_data)
#
#
