Array.prototype.groupBy = function (fn) {
    const groupedArray = {};
    this.forEach(item => {
      const key = fn(item);
      if (!groupedArray[key]) {
        groupedArray[key] = [];
      }
      groupedArray[key].push(item);
    });
    return groupedArray;
  };
  
  // Example 1
  const array1 = [
    { "id": "1" },
    { "id": "1" },
    { "id": "2" }
  ];
  const fn1 = function (item) {
    return item.id;
  };
  console.log(array1.groupBy(fn1));
  
  // Example 2
  const array2 = [
    [1, 2, 3],
    [1, 3, 5],
    [1, 5, 9]
  ];
  const fn2 = function (list) {
    return String(list[0]);
  };
  console.log(array2.groupBy(fn2));
  
  // Example 3
  const array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const fn3 = function (n) {
    return String(n > 5);
  };
  console.log(array3.groupBy(fn3));
  