#!/usr/bin/python3

import json
from urllib import response
from jsonpath_rw import jsonpath, parse
import click
import requests
import csv
from datetime import datetime


@click.command()
##@click.option('-u', required=True, type=str)
@click.option('-m', required=True, type=str)
@click.option('-s', required=True, type=str)
@click.option('-k', required=True, type=str)



def hello(m, s, k):

    with open(m) as data_csv:
        csv_data = csv.reader(data_csv)

        for row in csv_data:
            now = datetime.now()
            a = now.strftime("%d_%m_%Y.%H_%M_%S")
            b = now.strftime("%d_%m_%Y.%H_%M_%S")
            a = a + ' ||| ' + row[0] + ' Started'
            print(a, end='\r')



            r =requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + row[0] +
            '&strategy=' + s +
            '&key=' + k)
            responseJson = r.json()

            lcp_Exp = parse('$.lighthouseResult.audits["largest-contentful-paint"].numericValue')
            lcp = lcp_Exp.find(responseJson)

            cls_Exp = parse('$.lighthouseResult.audits["cumulative-layout-shift"].numericValue')
            cls = cls_Exp.find(responseJson)

            tbt_Exp = parse('$.lighthouseResult.audits["total-blocking-time"].numericValue')
            tbt = tbt_Exp.find(responseJson)

            a = b + ' ||| ' + str(row[0]) + ' ||| LCP = ' + str(lcp[0].value) + ' ||| CLS = ' + str(cls[0].value) + ' ||| TBT = ' + str(tbt[0].value)

            print(a)
            
           

 
if __name__ == '__main__':
    hello()