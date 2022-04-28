
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
/*
var name = prompt('whats your  name?')
greetingName(name)

var num = 0
while (num < 100) {
    num ++ 
    console.log(num)
}
*/
// for loop 
for (let num=0; num <= 100 ; num ++){
    console.log(num)
}

// Data Types

let yourAge = 18 // number 
let yourName = 'Bob' // string 
let nam = {first: 'jane', last :'Doe'}; // object 
let truth = false; // Boolean 
let groceries = ['apple', 'banana', 'oranges']; // array 

let random ; //undefined 
let nothing = null; // value null 

// String in Javascript (common methods)
let fruit = 'apple'
let moreFruit = 'banana\napple' // new line

console.log(moreFruit);
console.log(fruit.length);

console.log(fruit.indexOf('nan'));
console.log(fruit.slice(2,6))
console.log(fruit.replace('pple','ge'))
console.log(fruit.toLowerCase())
console.log(fruit.toUpperCase())

console.log(fruit.charCodeAt(2))
console.log(fruit[2])
console.log(fruit.split(''))


// array 
let fruits = ['banana', 'apple', 'orange', 'pineapples']
fruits = new Array('banana', 'apple', 'orange', 'pineapples')

console.log(fruits[2])

fruits[0] = 'pear'
console.log(fruits) 

for (let i = 0 ; i< fruits.length; i++){
    console.log(fruits[i])
}

console.log('to string', fruits.toString())

console.log(fruits.join('*'))

console.log(fruits, fruits.pop() , fruits)
console.log(fruits, fruits.push('blackberries') , fruits)
fruits[4] = 'new fruit'
console.log(fruits)

fruits.shift() // remove first element from a list
console.log(fruits)
fruits.unshift('kiwi') // add first element to an array 
console.log(fruits)
console.log('*' * 20)

let vegetables = ['asparagus', 'tomato', 'broccoli']
let allGroceries = fruits.concat(vegetables)
console.log(allGroceries)
console.log(allGroceries.slice(1, 4 ))
console.log(allGroceries.reverse())

let someNumber = [5 ,10, 2, 25, 235, 1, 2, 5, 234, 321, 2]

console.log(someNumber.sort(function(a,b) {return a-b}))

console.log(someNumber.sort(function(a,b) {return b-a}))


let emptyArray = new Array()
for (let num = 0; num < 10; num++){
    emptyArray.push(num)
}
console.log(emptyArray)

// Objects in Javascript 
// dict in Python

let student = {
    first:'Rafeh',
    last: 'Qazi',
    age: 25,
    height : 170,
    studentInfo: function(){
        return this.first + '\n' + this.last + '\n' + this.age
    }
}
console.log(student.first)
console.log(student.last)

console.log('-----------------------')
student.first = 'notRafeh'
console.log(student.first)


console.log(student.studentInfo())