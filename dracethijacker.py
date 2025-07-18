#!/usr/bin/python

#welcome to dracethijacker | created by draco

import optparse
import string
import subprocess as sp
from bs4 import BeautifulSoup as bs
import time , datetime , os
from tqdm import tqdm

def prvtkeyhijacker():
    parser = optparse.OptionParser()
    parser.add_option("-a","--address",dest="ethaddr",help="Enter the ethereum address for crack to private key")
    options,ags = parser.parse_args()

    os.system("clear")
    date = datetime.datetime.now()
    print(f"Starting Dracethijacker at {date} UTC\n")
    

    def scraper():
        global ethaddr
        try:
            spage,lpage = 1,1929868153955269923726183083478131797547292737984581739710086052358636024907

            for i in range(spage,lpage):

                url = f"curl -s https://privatekeyfinder.io/private-keys/ethereum/{i}"
                source = sp.check_output( url,shell=True,text=False)
                soup = bs(str( source),'html.parser')
                scrap =  soup.find("tbody")

                while scrap == None:

                    url = f"curl -s https://privatekeyfinder.io/private-keys/ethereum/{i}"
                    source = sp.check_output( url,shell=True,text=False)
                    soup = bs(str( source),'html.parser')
                    scrap =  soup.find("tbody")
                
                text =  scrap.get_text().replace("HEX","").replace(" ","").replace("Keyrangestart","").replace("Keyrangeend","").replace(r"\n","\t").split()
                scraped = " - ".join( text).replace(" - 0 - ","\n").lower()
                retext = scraped.splitlines()
                lenoflist = len(retext)
                for i in range(lenoflist):
                    if ethaddr in retext[i]:
                        print(f"PRIVATE KEY FOUNDED : {retext[i]}")
                        exit()
                else:
                    for t in tqdm(range(1),desc="PROCESSING"):
                        time.sleep(0.1)
                        if i==( lpage-1):
                            print("private key not found!")

        except KeyboardInterrupt:
            print("exiting...")
        except sp.CalledProcessError:
            print("[err]:network issue")
        except Exception as e:
            print(f"[err]:{e}")

    def validator():
        global ethaddr

        while True:
            try:
                ethaddr = (options.ethaddr).lower()
            except AttributeError:
                print("[err] : arguments couldn't find try '-h'")
                exit()
            except Exception as e:
                print(e)
            ethaddrvalidation = all(i in string.hexdigits for i in  ethaddr[2:])
            if len( ethaddr) == 42:
                if  ethaddrvalidation == True:
                    if  ethaddr[0] == "0" and  ethaddr[1] == "x":
                        scraper()
                        break
                    else:
                        print("[err] : invalid ethereum address , address starts with '0x'")
                        continue
                else:
                    print("[err] : invalid ethereum address , hex is only contain [0-9,a-f]")
                    continue
            else:
                print("[err] : invalid ethereum address , hex length is 42 char")
                continue

    validator()
prvtkeyhijacker()