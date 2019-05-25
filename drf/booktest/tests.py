# 设置Django运行所依赖环境变量
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf.settings")

# 让Django环境进行一次初始化
import django
django.setup()

import json
from booktest.models import BookInfo,HeroInfo
from booktest.serializers import HeroInfoSerializer,BookInfoSerializer

if __name__ == "__main__":
    # 获取id为1的图书
    book = BookInfo.objects.get(id=1)

    # 准备数据
    data = {'btitle': '射雕英雄传-2', 'bpub_date': '2000-01-01'}

    # 创建序列化器对象
    serializer = BookInfoSerializer(book, data=data)

    # 反序列化-数据校验
    res = serializer.is_valid()
    print(res)

    # 反序列化-数据保存(调用序列化器类中update)
    serializer.save()

    # 获取更新对象序列化之后的数据
    print(serializer.data)