
var chunk = function(arr, size) {
    const ans = [];
    let i = 0;

    while (i < arr.length) {
        const a = [];

        for (let j = i; j < i + size && j < arr.length; j++) {
            a.push(arr[j]);
        }

        ans.push(a);
        i += size;
    }

    return ans;
};

var isEmpty = function(obj) {
    const x=Object.keys(obj);
    if (x.length>0){
        return false;
    }
    return true;
};

const arr=[1, 2, 3, 4, 5, 6, 7, 8];
const result1 = chunk(arr, 3);
const result2 = isEmpty(arr)
console.log(result1);
console.log(result2);
