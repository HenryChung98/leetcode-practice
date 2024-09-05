var twoSum = function(nums, target) {
    let init = 1
    for (let i = 0; i < nums.length; i++){
        for (let j = init; j< nums.length; j++){
            if (nums[i] + nums[j] == target){
                var answer = new Array();
                answer[0] = i
                answer[1] = j
                return answer
            }
        }
        init++;
    }
    return 0;
};


arr = [3, 2, 3]
tar = 6
console.log(twoSum(arr, tar))