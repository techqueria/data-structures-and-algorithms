//my code was not originally this clean, but same concept as solution
function URLify(arr, len) {
	let spaces = 0;
	for(let i = 0; i < len; i++) {
		if(arr[i] === ' ') spaces++;  	
	}	
	//last index
	let index = len + spaces * 2 - 1;

	for(let i = len - 1; i >= 0; i--) {
		if(arr[i] === ' ') {
			arr[index] = '0'; 
			arr[index - 1] = '2';
			arr[index - 2] = '%';
			index -= 3
		} else {
			arr[index] = arr[i];
			index--;
		}	
	}
	return arr;
}

//testing
let arr = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' '];
//before
console.log(arr);
let ans = URLify(arr, 13);
//after
console.log(ans);
