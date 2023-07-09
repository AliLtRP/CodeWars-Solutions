let sumDigits = number => {
    number = new String(number);

    let result = 0;

    let x = [...number].map(Number).filter(i => {
            if(i === Number(i)){
                x+=i;
            }
        
    });
    
    return result;
}