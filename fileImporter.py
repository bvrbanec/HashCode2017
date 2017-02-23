#endpointsLatencyDataCentar = {'0':1000,'1':500}
#endpointsCacheLatency=[{'0':100,'2':200,'1':300},{}]

#requests= {'0':{'3':1500,'4':500, '1':1000},
          #'1':{'0':1000}}
def importFile(name):
    count=0

    with open(name) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

        #first line
        mySystem = lines[0].split(' ')
        numberOfVideos = mySystem[0]

        numberOfEndpoints = mySystem[1]

        endpointsCacheLatency = [dict() for x in range(int(numberOfEndpoints))]

        requestDesc = mySystem[2]

        caches = mySystem[3]
        cashCapacity = mySystem[4]

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

    # print "DataCenter:",endpointsLatencyDataCentar
    # print "CacheLatency", endpointsCacheLatency
    # print "Requests", requests