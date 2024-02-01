function memoize(fn) {
    const cache = new Map();
    const callCount = { count: 0 };
  
    function memoizedFunction(...args) {
      const key = JSON.stringify(args);
  
      if (cache.has(key)) {
        return cache.get(key);
      }
  
      callCount.count++;
      const result = fn(...args);
      cache.set(key, result);
  
      return result;
    }
  
    memoizedFunction.getCallCount = () => callCount.count;
  
    return memoizedFunction;
  }
  
  // Test cases
  const sum = (a, b) => a + b;
  const memoizedSum = memoize(sum);
  console.log(memoizedSum(2, 2)); // Output: 4
  console.log(memoizedSum(2, 2)); // Output: 4
  console.log(memoizedSum.getCallCount()); // Output: 1
  console.log(memoizedSum(1, 2)); // Output: 3
  console.log(memoizedSum.getCallCount()); // Output: 2
  
  const factorial = (n) => (n <= 1) ? 1 : (n * factorial(n - 1));
  const memoFactorial = memoize(factorial);
  console.log(memoFactorial(2)); // Output: 2
  console.log(memoFactorial(3)); // Output: 6
  console.log(memoFactorial(2)); // Output: 2
  console.log(memoFactorial.getCallCount()); // Output: 2
  console.log(memoFactorial(3)); // Output: 6
  console.log(memoFactorial.getCallCount()); // Output: 2
  
  const fib = (n) => (n <= 1) ? 1 : (fib(n - 1) + fib(n - 2));
  const memoFib = memoize(fib);
  console.log(memoFib(5)); // Output: 8
  console.log(memoFib.getCallCount()); // Output: 1
  