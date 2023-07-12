let isDivisibleBy6 = (s) => {
    let result = [];

    for (let i = 0; i < 10; i++) {
        let res = s;
        res = res.replace('*', i);

        if(res%6 == 0){
            result.push(res);
        }

    }

    console.log(result);
    return result;
}


isDivisibleBy6("12345678901200456789012040608*0");
