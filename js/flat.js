var flat1 = function (arr, n) {
    return arr.flat(n);
};
/**
 * Flattens a multi-dimensional array up to the specified depth.
 * @param {Array} arr - The input array.
 * @param {number} n - The depth up to which to flatten.
 * @returns {Array} - The flattened array.
 */
function flattenDeep(arr, n) {
    const result = [];

    for (const item of arr) {
        if (Array.isArray(item) && n > 0) {
            // Recursively flatten sub-arrays
            result.push(...flattenDeep(item, n - 1));
        } else {
            // Add non-array elements directly
            result.push(item);
        }
    }

    return result;
}

// Example usage:
const arr1 = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
const n1 = 0;
console.log(flattenDeep(arr1, n1)); // Output: [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

const arr2 = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
const n2 = 1;
console.log(flattenDeep(arr2, n2)); // Output: [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]

const arr3 = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
const n3 = 2;
console.log(flattenDeep(arr3, n3)); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
