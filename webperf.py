#!/usr/bin/python3

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
    click.echo(r.status_code)



 
if __name__ == '__main__':
    hello()