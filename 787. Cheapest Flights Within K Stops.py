# 787. Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p 
            prices = temp_prices

        return prices[dst] if prices[dst]!=float('inf') else -1
        # Time complexity - O(v+k)
        # Solved using Bellman-Ford Algorithm