#!/usr/bin/python3

import json
from urllib import response
from jsonpath_rw import jsonpath, parse
import click
import requests


@click.command()
@click.option('-u', required=True, type=str)
@click.option('-s', required=True, type=str)
@click.option('-k', required=True, type=str)

def hello(u, s, k):
    r =requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + u 
    + '&strategy=' + s
    + '&key=' + k)
    responseJson = r.json()

    lcp_Exp = parse('$.lighthouseResult.audits["largest-contentful-paint"].numericValue')
    lcp = lcp_Exp.find(responseJson)

    
    
    print(lcp[0].value)



 
if __name__ == '__main__':
    hello()