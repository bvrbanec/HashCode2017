
count=0

with open("kittens.in") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    #first line
    mySystem = lines[0].split(' ')
    numberOfVideos = mySystem[0]

    numberOfEndpoints = mySystem[1]

    endpointsCacheLatency = [dict() for x in range(int(numberOfEndpoints))]

    requestDesc = mySystem[2]

    caches = int(mySystem[3])
    cacheCapacity = int(mySystem[4])

    #video sizes
    videos = lines[1].split(' ')
    videos = map(int, videos)

    #reading endpoints with their characteristics
    more = True
    currentIndexInLines = 2
    endpointCounter = 0
    endpointsLatencyDataCentar ={}

    while more :
        #take endpoint with datacenter and number of caches connected
        currentEndpoint = lines[currentIndexInLines]
        currentIndexInLines += 1
        currentEndpoint = currentEndpoint.split(' ')

        #DataCenterlatency
        endpointsLatencyDataCentar[endpointCounter] = currentEndpoint[0]
        numberOfCashesForEndpoint = currentEndpoint[1]

        # print "endpoint has caches: ", numberOfCashesForEndpoint

        for x in range(1,int(numberOfCashesForEndpoint)+1):
            cacheLatency=lines[currentIndexInLines]
            cacheLatency = cacheLatency.split(' ')
            # print cacheLatency
            cache = cacheLatency[0]
            latency= cacheLatency[1]
            # print endpointCounter," ", cache, " ", latency

            endpointsCacheLatency[endpointCounter][cache]=latency
            currentIndexInLines +=1

        endpointCounter +=1
        if int(endpointCounter)==int(numberOfEndpoints):
            more = False
            break;

    # print "final line of endpoints", currentIndexInLines
    #process requests
    requests = [dict() for x in range(int(numberOfEndpoints))]
    for x in range(1, int(requestDesc) + 1):
        request = lines[currentIndexInLines]
        request = request.split(' ')
        videoNum = int(request[0])
        endpointNum= int(request[1])
        requestsNum = int(request[2])
        # print videoNum, "", endpointNum, "", requestsNum
        # print request
        requests[endpointNum][videoNum] = requestsNum
        currentIndexInLines+=1

    requestHelp = {}
    for index in range(len(requests)):
        requestHelp[str(index)]=requests[index]
    requests=requestHelp

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
                result += endpoitnRequest[k] * int(endpointsCacheLatency[int(endpoint)][str(server)])

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
