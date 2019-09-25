var containsNearbyDuplicate = function(nums,k){
    const visted = {}
    for (let i = 0;i<nums.length;i++){
        const num = nums[i];
        if (visted[num] !== undefined && i -visted[num] <=k){
            return true;
        }
        visted[num] = i;
    }
    return false
}