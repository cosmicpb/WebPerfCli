#!/usr/bin/python3

from asyncore import write
import json
from urllib import response
from jsonpath_rw import jsonpath, parse
import click
import requests
import csv
from csv import writer
from datetime import datetime
import gui


@click.command()
@click.option('-d', required=True, type=str)
@click.option('-s', required=True, type=str)
@click.option('-k', required=True, type=str)
@click.option('-o', type=str)

def func(d, s, k, o):

    gui.hellogui(d,s,o)

    count = 0   
    
    with open(d) as data_csv:
        csv_data = csv.reader(data_csv)

        for row in csv_data:
            ##output = open(o, 'a')
            now = datetime.now()
            a = now.strftime("%d_%m_%Y.%H_%M_%S")
            b = now.strftime("%d_%m_%Y.%H_%M_%S")
            a = a + ' ||| ' + row[0] + ' Started'
            print(a, end='\r')

            r =requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + row[0] +
            '&strategy=' + s +
            '&key=' + k)

            if(r.status_code>=400):

                responseJson = r.json()

                message_Exp = parse('$.error.message')
                msg = message_Exp.find(responseJson)

                
                c = b + ' ||| ' + str(row[0]) + ' ERROR. Status Code = ' + str(r.status_code) + '  ' + msg[0].value
                print(c)

                if(o):
                    with open(o, 'a', newline='') as output:
                        webvitals = [b, str(row[0]), r.status_code, 'ERROR', 'ERROR', 'ERROR']
                        wrt = writer(output)
                        wrt.writerow(webvitals)
                    
                
    
            else:

                responseJson = r.json()

                lcp_Exp = parse('$.originLoadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.percentile')
                lcp = lcp_Exp.find(responseJson)

                cls_Exp = parse('$.originLoadingExperience.metrics.CUMULATIVE_LAYOUT_SHIFT_SCORE.percentile')
                cls = cls_Exp.find(responseJson)

                tbt_Exp = parse('$.originLoadingExperience.metrics.FIRST_INPUT_DELAY_MS.percentile')
                tbt = tbt_Exp.find(responseJson)

                
                
                if(o):
                    with open(o, 'a', newline='') as output:
                        webvitals = [b, str(row[0]), r.status_code, str(lcp[0].value), str(cls[0].value/100), str(tbt[0].value)]
                        wrt = writer(output)
                        wrt.writerow(webvitals)
                              

                a = b + ' ||| ' + str(row[0]) + ' ||| LCP = ' + str(lcp[0].value) + ' ||| CLS = ' + str(cls[0].value/100) + ' ||| FID = ' + str(tbt[0].value)

                print(a)
               
           

 
if __name__ == '__main__':
    
    func()