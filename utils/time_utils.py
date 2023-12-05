#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time


def get_current_time_in_mills():
    return int(round(time.time() * 1000))


def get_time_in_mills_by_time_in_seconds(time_in_second):
    return int(round(time_in_second * 1000))
