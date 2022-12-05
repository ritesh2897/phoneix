import json

from django.forms import ModelForm
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers
from rest_framework.response import Response

from data.models import Data, Subscriber, Post, Request
from data.models_ import models_
from identity.views import ConstrainUserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_on']


class DataSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Data
        fields = ['id', 'title', 'options', 'api', 'data', 'result', 'status', 'created_on', 'updated_on', 'posts']


# Create the form class.
class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_on']

    def create(self, request, *args, **kwargs):
        data_ = request.data
        options = json.loads(data_["options"])
        res = models_(data=data_["data"], api=data_["api"], **options) or []
        if hasattr(request.data, '_mutable'):
            request.data._mutable = True
        request.data.update({'result': json.dumps(res)})
        data_form = DataForm(data_)
        data = data_form.save()
        posts = []
        for post in res:
            posts.append(Post.objects.create(data=data, content=post))
        data.posts.set(posts)
        data_serializer = DataSerializer(data)
        return Response(data_serializer.data)


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(response)
        response['user'] = ConstrainUserSerializer(instance.user).data
        return response


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_on']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(response)
        response['user'] = ConstrainUserSerializer(instance.user).data
        return response


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_on']
