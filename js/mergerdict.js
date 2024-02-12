/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    // Create an empty object to store merged objects based on id
    const result = {};

    // Merge arr1 into the result object
    for (let i = 0; i < arr1.length; i++) {
        result[arr1[i].id] = arr1[i];
    }

    // Merge arr2 into the result object, overriding values from arr1
    for (let i = 0; i < arr2.length; i++) {
        // Check if the id from arr2 already exists in result
        if (result[arr2[i].id]) {
            // If yes, merge the two objects
            for (const key in arr2[i]) {
                result[arr2[i].id][key] = arr2[i][key];
            }
        } else {
            // If no, add the object to the result object
            result[arr2[i].id] = arr2[i];
        }
    }

    // Convert the values of the result object to an array
    return Object.values(result);
};

//Example usage:
arr1 = [
    {"id": 1, "x": 2, "y": 3},
    {"id": 2, "x": 3, "y": 6}
]

arr2 = [
    {"id": 2, "x": 10, "y": 20},
    {"id": 3, "x": 0, "y": 0}
]

result1 = join(arr1, arr2)
console.log(result1)