const myPromise = new Promise((resolve, reject) => {
  const successfulOperation = true;

  if (successfulOperation) {
    resolve("Operation successful");
  } else {
    reject("Operation failed");
  }
});

myPromise
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });


/*
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */

var addTwoPromises = async function(promise1, promise2) {
  const a=await promise1;
  const b=await promise2;
  return a+b;
};

var addTwoPromises = async function(promise1, promise2) {
  const [result1, result2] = await Promise.all([promise1, promise2]);
  return result1 + result2;
};




/**
* addTwoPromises(Promise.resolve(2), Promise.resolve(2))
*   .then(console.log); // 4
*/