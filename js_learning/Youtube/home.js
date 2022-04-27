
console.log('hello');

// alter('hello this is qazi')


var b = 'smoothie';

console.log(b);

// var someNumber = 45;
// console.log(someNumber)

// document.getElementById('someText').innerHTML = 'Hello, hey Here'

// var age = prompt('what is your age?');
// document.getElementById('age').innerHTML = age

var num1 = 5.7;
num1 = num1 + 1 
console.log(num1)

num1 ++ 
console.log(num1)

console.log(num1 % 5)

console.log(num1 % 2)


function fun() {
    console.log('this is functions!')
}
fun();


function greeting() {
    var name = prompt('whats your name')
    var result = 'hello ' + name 
    console.log(result)
}

function addNum(a, b) {
    var result = a + b 
    console.log(result)
}

function greetingName(name) {
    var result = 'hello ' + name 
    console.log(result)
}

var name = prompt('whats your  name?')
greetingName(name)