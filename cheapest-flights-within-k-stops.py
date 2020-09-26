# currently my data is in the form [[0, 1, 100], [1, 2, 100]]
# in order to make this easier to evaluate, I want my data to be in the form {{0 : {1, 100}}, {1 : {2, 100}}}
# 

# next thing I need is to go through the neighbors and evaluate
#my constraints --> I want to stop when I hit my destination
# I want to stop if I have made the number of stops
# to do that, I know I need to make a priority queue and go through the neighboring vertices
#what info do I need to make the queue work? 
# need to update the price as we go along, and number of stops we've made (where we've visited)


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        for i in range(0, len(flights)):
            graph = []
        for src, neighbor, cost in flights:
            graph[src] = neighbor, cost
            print(graph)
        #now I need to go through the neighbors and make the priority queue
        #queue = [vertex, total cost, number of stops taken]
        flightqueue = [(src, 0, 0)]
        
        while flightqueue:
            #have we reached our destination?
            vertex, totalCost, numStops = heapq.heappop(flightqueue)
            if vertex == dst:
                return totalCost
            #have we reached the number of stops?
            if numStops > K:
                pass
            #now we move on to our neighbor, so we have to use the other graph to get it
            for vertex, neighbor, cost in graph:
                heapq.heappush(flightqueue, [neighbor, totalCost + cost, numStops + 1])

                
            
        
        return -1
        