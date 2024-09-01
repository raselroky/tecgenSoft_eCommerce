from campaign.models import CampaignMember,Campaign,DealOfTheWeek
from typing import (
    List, 
    Callable,
    Any, 
    Type,
    Dict
)

def get_overall_discount_calculated_values(obj,selling_price):
    discount=0
    #print('selling',selling_price)
    cmpm=CampaignMember.objects.filter(product_variant__id=obj)
    deal=DealOfTheWeek.objects.filter(product_variant__id=obj)
    
    if cmpm and not deal:
        result=0
        campaign_member = CampaignMember.objects.filter(product_variant__id=obj).first()
        #print('member',campaign_member)
        if campaign_member.discount_type == "percentage":
            result = float(selling_price-float(selling_price * (campaign_member.discount_value / 100) ))
        elif(campaign_member.discount_type == "flat"):
            result = selling_price-float(campaign_member.discount_value)
        
        return result
    elif deal and not cmpm:
        result=0
        deal_of_the_week=DealOfTheWeek.objects.filter(product_variant__id=obj).first()
        if deal_of_the_week.discount_type == 'percentage':
            result = float(selling_price-float(selling_price * (deal_of_the_week.discount_value / 100) ))
        else:
            result = selling_price-float(deal_of_the_week.discount_value)
        #print('result',result)
        return result
    else:
        return discount
    
    
def entries_to_remove(data: dict, removeable_keys: tuple) -> dict:
    for k in removeable_keys:
        data.pop(k, None)
    return data


def remove_duplicate_from_list(iterable: List, key:  Callable = None) ->List:
    if key is None:
        def key(x): return x

    seen = set()
    for elem in iterable:
        k = key(elem)
        if k in seen:
            continue

        yield elem
        seen.add(k)


