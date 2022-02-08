#
#
#   s3sec developed by 0xmoot
#
#   Test AWS S3 instances for read/write/delete access
#   Usage: cat locations | python3 s3sec.py
#
#   0xmoot.com
#   twitter.com/0xmoot
#
#   Found a bug bounty using this tool? Feel free to add me as a collaborator: 0xmoot
#
#

import sys
import requests
import subprocess
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("     _____               ", file=sys.stderr)
print(" ___|___ / ___  ___  ___ ", file=sys.stderr)
print("/ __| |_ \/ __|/ _ \/ __|", file=sys.stderr)
print("\__ \___) \__ \  __/ (__ ", file=sys.stderr)
print("|___/____/|___/\___|\___|", file=sys.stderr)
print("", file=sys.stderr)
print("	0xmoot.com", file=sys.stderr)
print("	twitter.com/0xmoot", file=sys.stderr)
print("", file=sys.stderr)
print("Found a bug bounty using this tool?", file=sys.stderr)
print("Feel free to add me as a collaborator: 0xmoot :)", file=sys.stderr)
print("", file=sys.stderr)
print("Disclaimer: Use with caution. You are responsible for your actions.", file=sys.stderr)
print("Developers assume no liability and are not responsible for any misuse or damage.", file=sys.stderr)
print("Usage: cat locations | python3 s3sec.py", file=sys.stderr)
print("", file=sys.stderr)

class http_obj:
    status_code: int
    text: str
    _url: str

def http_get(url):

    data = http_obj()
    data._url = url
    data.text = ""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'connection': 'close'
    }

    try:
        r = requests.get(url, headers=headers, verify=False, timeout=3)
        data.status_code = r.status_code
        data.text = r.text
    except:
        data.status_code = -1
    
    return data

added = []
def process(url, protocol="https"):

    b = http_get(protocol+"://"+url+".s3.amazonaws.com")

    if(b.text.find("<Error><Code>")>=0):
        code = b.text.split("<Error><Code>")[1].split("</Code>")[0]
        print(url+".s3.amazonaws.com [error: "+code+"]")
        if(code == "AccessDenied"):
            try:
                #falls back to aws cli to test access with --no-sign-request argument
                subprocess.check_output([str('aws'), 's3', 'ls', 's3://'+url, '--no-sign-request'],stderr=subprocess.DEVNULL)
                print(url+".s3.amazonaws.com [read (--no-sign-request)]")
            except:
                return
        return
    elif(b.text.find("ListBucketResult")>=0):
        print(url+".s3.amazonaws.com [read]")
    else:
        if(protocol=="http"):
            print(url+".s3.amazonaws.com [error: ConnectionError("+str(b.status_code)+")]")
        else:
            #try connecting to http instead
            process(url,"http")
        return

    try:
        #check that we can write to server
        subprocess.check_output([str('aws'), 's3', 'cp', os.getcwd()+"/s3sec.txt", 's3://'+url+'/s3sec.txt', '--no-sign-request'],stderr=subprocess.DEVNULL)
        print(url+".s3.amazonaws.com [write]")

        #check that we can remove file from server
        subprocess.check_output([str('aws'), 's3', 'rm', 's3://'+url+'/s3sec.txt', '--no-sign-request'],stderr=subprocess.DEVNULL)
        print(url+".s3.amazonaws.com [delete]")

    except:
        return

urls = []; c = 0
for line in sys.stdin:
    url = line.strip().replace("https://","").replace(".s3.amazonaws.com","").replace("s3.amazonaws.com/","")
    process(url)
