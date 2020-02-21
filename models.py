# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Addressinfo(models.Model):
    add = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'addressinfo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ctweather(models.Model):
    aqi = models.TextField(blank=True, null=True)
    avgtmp = models.TextField(db_column='avgTmp', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(blank=True, null=True)
    cloudamount = models.TextField(db_column='cloudAmount', blank=True, null=True)  # Field name made lowercase.
    datatime = models.TextField(db_column='dataTime', blank=True, null=True)  # Field name made lowercase.
    humi = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    mainpol = models.TextField(db_column='mainPol', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.TextField(blank=True, null=True)
    vis = models.TextField(blank=True, null=True)
    windlevel = models.TextField(db_column='windLevel', blank=True, null=True)  # Field name made lowercase.
    windspeed = models.TextField(db_column='windSpeed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ctweather'


class Disweather(models.Model):
    aqi = models.TextField(blank=True, null=True)
    avgtmp = models.TextField(db_column='avgTmp', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(blank=True, null=True)
    cloudamount = models.TextField(db_column='cloudAmount', blank=True, null=True)  # Field name made lowercase.
    datatime = models.TextField(db_column='dataTime', blank=True, null=True)  # Field name made lowercase.
    humi = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    mainpol = models.TextField(db_column='mainPol', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.TextField(blank=True, null=True)
    vis = models.TextField(blank=True, null=True)
    windlevel = models.TextField(db_column='windLevel', blank=True, null=True)  # Field name made lowercase.
    windspeed = models.TextField(db_column='windSpeed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disweather'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LearnCnyNum(models.Model):
    data = models.IntegerField(primary_key=True)
    sr = models.IntegerField()
    zc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'learn_cny_num'


class Mayun(models.Model):
    weibo_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255, blank=True, null=True)
    uid_name = models.CharField(max_length=255, blank=True, null=True)
    dianzan = models.CharField(max_length=255, blank=True, null=True)
    huifu = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mayun'


class NewWeibo(models.Model):
    weibo_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255, blank=True, null=True)
    uid_name = models.CharField(max_length=255, blank=True, null=True)
    dianzan = models.CharField(max_length=255, blank=True, null=True)
    huifu = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    fenci = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_weibo'


class Odmatrix(models.Model):
    x = models.CharField(db_column='X')  # Field name made lowercase.
    y = models.CharField(db_column='Y')  # Field name made lowercase.
    ids = models.CharField(db_column='IDS', max_length=11)  # Field name made lowercase.
    oddate = models.CharField(db_column='ODDATE')  # Field name made lowercase.
    odtime = models.CharField(db_column='ODTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odmatrix'


class Userinfo(models.Model):
    name = models.CharField(max_length=20)
    addinfo = models.ForeignKey(Addressinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userinfo'


class Weibo(models.Model):
    weibo_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255, blank=True, null=True)
    uid_name = models.CharField(max_length=255, blank=True, null=True)
    dianzan = models.CharField(max_length=255, blank=True, null=True)
    huifu = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    seg_word = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'weibo'


class Weibo0511(models.Model):
    weibo_user_name = models.CharField(max_length=255, blank=True, null=True)
    repost_user_name = models.CharField(max_length=255, blank=True, null=True)
    publish_time = models.CharField(max_length=255, blank=True, null=True)
    weibo_item_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weibo0511'


class Weibo0516(models.Model):
    weibo_user_name = models.CharField(max_length=255, blank=True, null=True)
    repost_user_name = models.CharField(max_length=255, blank=True, null=True)
    publish_time = models.CharField(max_length=255, blank=True, null=True)
    weibo_repost = models.CharField(max_length=255, blank=True, null=True)
    weibo_item_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weibo0516'


class Weibo06132CopyClean(models.Model):
    c_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.CharField(max_length=255, blank=True, null=True)
    uid_name = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    dianzan = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    img1 = models.CharField(max_length=255, blank=True, null=True)
    img2 = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    co_clean = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weibo0613_2_copy_clean'
