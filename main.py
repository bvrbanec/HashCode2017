numberOfVideos=5
numberOfendpoints= 2
requestDesc= 4
caches= 3
cacheCapacity= 100

videos= [50,50,80,30,110]
endpointsLatencyDataCentar = {'0':1000,'1':500}
endpointsCacheLatency=[{'0':100,'2':200,'1':300},{}]

requests= {'0':{'3':1500,'4':500, '1':1000},
          '1':{'0':1000, '1': 300}}

#videorequests = {'0': 1000, '1': 1300, '2': 0, '3' : 1500, '4': 500}

videorequests = {}

for endpoint, endpointRequest in requests.items():
    for video, numberOfRequests in endpointRequest.items():
        if not videorequests.has_key(video):
            videorequests[video] = 0
        videorequests[video] += numberOfRequests

import operator
sorted_x = sorted(videorequests.items(), key=operator.itemgetter(1))
sorted_x.reverse()

cacheServerSpaceLeft = [cacheCapacity] * caches

videoLatenciesCache = {}

for k, v in sorted_x:
    best = float('inf')
    bestCacheServer = 1;
    videoLatenciesCache[k] = {}

    for server in range(caches):
        result = 0

        for endpoint, endpoitnRequest in requests.items():
            if endpoitnRequest.has_key(k) and endpointsCacheLatency[int(endpoint)].has_key(str(server)):
                result += endpoitnRequest[k] * endpointsCacheLatency[int(endpoint)][str(server)]

        if result == 0:
            result = float('inf')

        videoLatenciesCache[k][str(server)] = result

#print videoLatenciesCache

videosStorage = {}


for video, Serverlatencies in videoLatenciesCache.items():
    sortedLatencies = sorted(Serverlatencies.items(), key=operator.itemgetter(1))

    for server, latency in sortedLatencies:
        if cacheServerSpaceLeft[int(server)] > videos[int(video)]:
            if not videosStorage.has_key(server):
                videosStorage[server] = list()

            videosStorage[server].append(video)
            break

#print videosStorage


#print number of used cache servers
print len(videosStorage.keys())

#
for server, videos in videosStorage.items():
    print server + ' ' + ' '.join(videos)
