var distributeCandies = function(candies){
    const count = new Set(candies)
    return Math.min(count.size,candies.length>>1)
}