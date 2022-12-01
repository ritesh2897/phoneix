import json

from rest_framework import viewsets, serializers
from data.models import Data, Subscriber, Post
from data.models_ import models_
from data.pagination import DataLimitPagination
from data.permission import MyPermission



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    pagination_class=DataLimitPagination
    permission_classes=[MyPermission]

    def create(self, request, *args, **kwargs):
        data_ = request.data
        options = json.loads(data_["options"])
        res = models_(data=data_["data"], api=data_["api"], **options)
        request.data._mutable = True
        request.data.update({'result': res})
        return super(DataViewSet, self).create(request, *args, **kwargs)


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
