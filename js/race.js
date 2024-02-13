function timeLimit(fn, t) {
    return async (...args) => {
        const timeoutPromise = new Promise((_, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        try {
            const result = await Promise.race([fn(...args), timeoutPromise]);
            return result;
        } catch (error) {
            throw error;
        }
    };
}

async function main() {
    try {
        const fn = async (n) => {
            await new Promise((res) => setTimeout(res, 100));
            return n * n;
        };

        const limited = timeLimit(fn, 50);

        const start = performance.now();
        let result;

        try {
            const res = await limited(5);
            result = { resolved: res, time: Math.floor(performance.now() - start) };
        } catch (err) {
            result = { rejected: err, time: Math.floor(performance.now() - start) };
        }

        console.log(result);
    } catch (error) {
        console.error(error);
    }
}

main();
