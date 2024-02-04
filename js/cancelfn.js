
const cancellable = function(fn, args, t) {
    // cancelFn function//
    const cancelFn = function (){
      clearTimeout(timer);
  };
  const timer = setTimeout(()=>{
      fn(...args)
  }, t);
  return cancelFn ;
};



var cancellable = function (fn, args, t) {
    let isCancelled = false;

    const cancelFn = () => {
        isCancelled = true;
    };

    const delayedExecution = () => {
        if (!isCancelled) {
            return fn(...args);
        } else {
            throw new Error("Operation was cancelled");
        }
    };

    const prom1 = new Promise((resolve) => {
        setTimeout(() => {
            resolve(delayedExecution());
        }, t);
    });

    return delayedExecution;
};

const fn = (x) => x * 5;
const args = [2];
const t = 20;
const cancelTimeMs = 50;

const cancelFn = cancellable(fn, args, t);
setTimeout(cancelFn, cancelTimeMs);
