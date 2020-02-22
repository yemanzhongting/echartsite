from django.db import models

# Create your models here.
class AddressInfo(models.Model):
    '''地址表
    类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度'''
    add=models.CharField(max_length=50)
    class Meta:
        #元类
        db_table = 'addressinfo'#定义数据表名称
        verbose_name = '地址管理'#在网页端显示的名字
        verbose_name_plural = verbose_name#去复数形式
    def __str__(self):
        return self.add

# Create your models here.
class VirusInfo(models.Model):
    '''地址表
    类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度'''
    name=models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    fromarea = models.CharField(max_length=50)
    temprature= models.IntegerField()
    tele=models.CharField(max_length=50)
    class Meta:
        #元类
        db_table = 'VirusInfo'#定义数据表名称
        verbose_name = '疫情人员统计'#在网页端显示的名字
        verbose_name_plural = verbose_name#去复数形式
    def __str__(self):
        return self.virus

class UserInfo(models.Model):
    """ 用户表 """
    name=models.CharField(max_length=20)
    addinfo=models.ForeignKey(AddressInfo)
    #这个是两张表之间的关系，关系写在从表身上，ForeignKey（）里面填写的是主表的类名
    class Meta:
        # 元类
        db_table = 'userinfo'
        verbose_name = '用户信息管理'
        verbose_name_plural = verbose_name
    def __str__ (self):
        return self.name

class WeiboInfo(models.Model):
    """ 用户表 """
    name=models.CharField(max_length=20)
    idinfo=models.ForeignKey(AddressInfo)
    vis=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    #这个是两张表之间的关系，关系写在从表身上，ForeignKey（）里面填写的是主表的类名
    class Meta:
        # 元类
        db_table = 'weiboinfo'
        verbose_name = '微博信息'
        verbose_name_plural = verbose_name
    def __str__ (self):
        return self.name

 # `id` INTEGER NOT NULL,
 #    `_id` VARBINARY(12),
 #    `name` LONGTEXT,
 #    `timenow` LONGTEXT,
 #    `addr` LONGTEXT,
 #    `txt` LONGTEXT,
 #    `repost` INTEGER,
 #    `comment` INTEGER,
 #    `thumb` INTEGER,
 #    PRIMARY KEY (`id`)

# Create your models here.
class coronavirus(models.Model):
  id = models.CharField(max_length=36,primary_key=True)
  name = models.CharField(max_length=30)
  timenow = models.CharField(max_length=30)
  addr = models.CharField(max_length=30)
  txt = models.CharField(max_length=300,null=True)
  repost = models.IntegerField()
  comment = models.IntegerField()
  thumb = models.IntegerField()

# class User(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.CharField(max_length=40)

# class
# data1 = AddressInfo.objects.get(add='北京')
# data1.delete()#使用任意查询语句后跟.delete()即可删除指定数据

# python manage.py makemigrations
# python manage.py migrate
