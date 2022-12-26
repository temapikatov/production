

import numpy as np
from django.db import models

class Baka(models.Model):
      name = models.CharField(max_length=200, null=True, blank=True)
      gender = models.BooleanField(null=True, blank=True)