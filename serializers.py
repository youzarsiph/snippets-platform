""" Serializers """


from snippets.models import Snippet
from rest_framework.serializers import ModelSerializer


class SnippetSerializer(ModelSerializer):
    """ Snippet Serializer """

    class Meta:
        """ Meta data """

        model = Snippet
        fields = ('id', 'user', 'name', 'extension', 'code')
