# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
# Create your models here.
class cny_num(models.Model):
    data = models.IntegerField(primary_key=True)
    sr = models.IntegerField()
    zc = models.IntegerField()

    def __unicode__(self):
        return '%s' % (self.name)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
