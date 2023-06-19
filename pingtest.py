import json
from urllib.request import urlopen
import ping3

OCI_URL = "https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json"
response = urlopen(OCI_URL)
jsondata = json.loads(response.read())
regions = jsondata['regions']

count = 5
results = open("results.csv", "w")

for region in regions:
    print ("Testing region: {} ".format(region['region']))
    r_total = 0
    results.write("{},".format(region['region']))
    for x in range(0,count):
        p = ping3.ping("objectstorage.{}.oraclecloud.com".format(region['region']), unit='ms')
        print ("{}: {} - {}".format(x+1, p, region['region']))
        results.write("{},".format(p))
        r_total = r_total + p
    print ("AVG of {}: {}ms".format(count, r_total/count))
    results.write("{}\n".format(r_total/count))

results.close()




