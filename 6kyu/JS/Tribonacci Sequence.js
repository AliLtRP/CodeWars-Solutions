function tribonacci(signature, n) {
    let arr = Array();
    arr.push(...signature);

    if (n === 0) {
        return Array();
    } else if (n < 3) {
        return [arr[n - 1]];
    }

    let len = 0;
    while (arr.length < n) {
        len = arr.length - 1;
        arr.push(arr[len] + arr[len - 1] + arr[len - 2]);
    }

    return arr;
}


tribonacci([1, 1, 1], 10);