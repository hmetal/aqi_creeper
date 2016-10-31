#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Qiu Peng
@contact: peng.qiup@alibaba-inc.com
@date: 2016-10-31 10:35
@version: 0.0.0
@license: Copyright alibaba-inc.com
@copyright: Copyright alibaba-inc.com

"""

import urllib, urllib2;
import sys, os;
import json;
import time;

buffer = {};

while True:
    url = 'http://222.83.228.210:8016/AQIDataService.ashx?action=GetRealTimeData';
    get_handle = urllib2.urlopen(url, timeout=1000);
    result = get_handle.read();
    get_handle.close();
    json_parser = json.loads(result);
    for site in json_parser:
        date = site['APIDATE'];
        siteName = site['DisplayName'];
        if date not in buffer:
            buffer[date] = {};
        if siteName not in buffer[date]:
            buffer[date][siteName] = [];
            buffer[date][siteName].append(site['AQI']);
            buffer[date][siteName].append(site['QUALITY']);
            buffer[date][siteName].append(site['PRIMARY']);
            buffer[date][siteName].append(site['PM25_1H']);
            buffer[date][siteName].append(site['PM25_24H']);
            buffer[date][siteName].append(site['PM10_1H']);
            buffer[date][siteName].append(site['PM10_24H']);
            buffer[date][siteName].append(site['SO2_1HAQI']);
            buffer[date][siteName].append(site["SO2_24HAQI"]);
            buffer[date][siteName].append(site["NO2_1HAQI"]);
            buffer[date][siteName].append(site["NO2_24HAQI"]);
            buffer[date][siteName].append(site["CO_1HAQI"]);
            buffer[date][siteName].append(site["O3_1H"]);
            buffer[date][siteName].append(site["O3_1H_24H"]);
            buffer[date][siteName].append(site["O3_8H"]);
            buffer[date][siteName].append(site["O3_8H_24H"]);
            for i in range(0, len(buffer[date][siteName])):
                if type(buffer[date][siteName][i]) in (int, float):
                    buffer[date][siteName][i] = str(buffer[date][siteName][i]);
            print '\t'.join([date,siteName] + buffer[date][siteName]);
    url = 'http://222.83.228.210:8016/AQIDataService.ashx?action=GetAvgHourData';
    get_handle = urllib2.urlopen(url);
    result = get_handle.read();
    get_handle.close();
    json_parser = json.loads(result);
    for site in json_parser:
        date = site["APIDATE"];
        siteName = u'全市';
        if date not in buffer:
            buffer[date] = {};
        if siteName not in buffer[date]:
            buffer[date][siteName] = []
            buffer[date][siteName].append(site['AQI']);
            buffer[date][siteName].append(site['Quality']);
            buffer[date][siteName].append(site['Pollutants']);
            buffer[date][siteName].append(site['PM25_1H']);
            buffer[date][siteName].append(site['PM25_24H']);
            buffer[date][siteName].append(site['PM10_1H']);
            buffer[date][siteName].append(site['PM10_24H']);
            buffer[date][siteName].append(site['SO2_1H']);
            buffer[date][siteName].append(site["NO2_1H"]);
            buffer[date][siteName].append(site["CO_1H"]);
            buffer[date][siteName].append(site["O3_1H"]);
            for i in range(0, len(buffer[date][siteName])):
                if type(buffer[date][siteName][i]) in (int, float):
                    buffer[date][siteName][i] = str(buffer[date][siteName][i]);
            print '\t'.join([date,siteName] + buffer[date][siteName]);
    time.sleep(1800);
