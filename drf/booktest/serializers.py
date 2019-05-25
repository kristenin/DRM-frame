from rest_framework import serializers
from booktest.models import BookInfo

class HeroInfoSerializer(serializers.Serializer):
    """英雄序列化器类"""
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    id = serializers.IntegerField(label='英雄id', read_only=True)
    hname = serializers.CharField(label='英雄名称', max_length=20)
    hgender = serializers.ChoiceField(label='性别', choices=GENDER_CHOICES, default=0)
    hcomment = serializers.CharField(label='评论', required=False)

    hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)


def about_django(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError('btitle必须含有django')
    return value

class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='图书id', read_only=True)
    btitle = serializers.CharField(label='图书标题', max_length=20)
    bpub_date = serializers.DateField(label='出版日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)

    def create(self, validated_data):
        """
        validated_data: 校验之后的数据，字典
        """
        book = BookInfo.objects.create(**validated_data)

        return book

    def update(self, instance, validated_data):
        """
        instance: 要更新对象
        validated_data: 校验之后的数据，字典
        """
        # 获取btitle和bpub_date
        btitle = validated_data.get('btitle')
        bpub_date = validated_data.get('bpub_date')

        # 更新数据
        instance.btitle = btitle
        instance.bpub_date = bpub_date
        instance.save()

        return instance