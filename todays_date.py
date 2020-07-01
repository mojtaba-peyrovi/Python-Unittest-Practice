# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:39:51 2020

@author: "mojtaba@heroleads.com"
"""

from datetime import datetime, timedelta

def return_todays_date():
    return datetime.today().date()


def return_yesterdays_date():
    date_ = datetime.today() - timedelta(days=1)
    return date_.date()


def check_date(sample):
    if sample.year != datetime.today().year:
        raise ValueError('Not current Year')
    else:
        return sample