var isPalindrome = function(x) {

    let str = x.toString();
    let left = 0, right = str.length - 1;

    while (left < right) {
        if (str[left] !== str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true
};


let a = 1212
console.log(isPalindrome(a))