from django.db import models
from user.models import Users

class CustomQuerySetManager(models.QuerySet):
    def filter_by_query(self,query_dict):
        return self.filter(**query_dict)
    
