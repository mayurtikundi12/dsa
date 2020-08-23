
// Takes theta(n) auxilarry space because of call stack hence not good solution
function find_factorial_reccursive(n){
    if(n==1){
        return 1;
    }
    return n * find_factorial_reccursive(n-1)
}

let result = find_factorial_reccursive(4);
console.log("Factorial using recursion => ",result);


// Takes theta(1) auxilary space hance good
function find_factorial_loop(n){
    let res = 1 ;
    for(let i=2;i<=n;i++){
        res*=i;
    }

    return res;
}

let result2 = find_factorial_loop(4)
console.log("factorial using loop => ",result2);
