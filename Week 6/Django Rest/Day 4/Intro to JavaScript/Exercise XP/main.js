const people = ["Greg", "Mary", "Devon", "James"];

// 1. Write code to remove “Greg” from the people array.

people.shift()

console.log(people)


// 2. Write code to replace “James” to “Jason”.

let newName = "Jason"

people[2] = newName

console.log(people)

// 3. Write code to add your name to the end of the people array.

people.push("David")

console.log(people)

// 4. Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

let x = people.indexOf("Mary")
console.log(x)

// 5. Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.

console.log(people.slice(1))

// 6. Write code that gives the index of “Foo”.

console.log(people.indexOf("Foo"))

people.forEach(element => { console.log(element)
    
});




