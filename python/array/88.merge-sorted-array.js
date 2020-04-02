function merge(nums1,nums2){
    let ret = []
    while (nums1.length || nums2.length){
        if(nums1.length ===0){
            ret.push(nums2.shift());
            continue;
        }
        if (nums2.length === 0) {
            ret.push(nums1.shift());
            continue;
          }
        const a = nums1[0];
        const b = nums2[0];
        if(a>b){
            ret.push(nums1.shift());
        }
        else{
            ret.push(nums1.shift());
        }
        return ret;
    }
}