numberOfVideos=5
numberOfendpoints= 2
requestDesc= 4
caches= 3
cashCapacity= 100

videos= [50,50,80,30,110]
endpointsLatencyDataCentar = {'0':1000,'1':500}
endpointsCacheLatency=[{'0':100,'2':200,'1':300},{}]

requests= {'0':{'3':1500,'4':500, '1':1000},
          '1':{'0':1000, '1': 300}}

videorequests = {'0': 1000, '1': 1300, '2': 0, '3' : 1500, '4': 500}#.sort(value, desc)
import operator
sorted_x = sorted(videorequests.items(), key=operator.itemgetter(1))
sorted_x.reverse()
for k, v in sorted_x:
    best = float('inf')
    bestCacheServer = 0;
    for server in range(caches):
        result =0
        for endpoint in requests.values():

            print k, v