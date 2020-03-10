function findElement(arr, func) {
  let num;
  for (let x = 0; x < arr.length; x++) {
    num = arr[x]
    if (func(arr[x]) === true) {
        return num;
    }
    
  }
  
  
}

console.log(findElement([1, 2, 3, 4], num => num % 2 === 0));
