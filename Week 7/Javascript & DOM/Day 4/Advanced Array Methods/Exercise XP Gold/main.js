// Exercise 1: Sum Elements

const theArray = [1, 20, 30, 40]

function summation (array) {
    sum = 0;

    for(let i=0; i < array.length; i++){
        sum += array[i];
    }

    return sum;
}

console.log(summation(theArray))

// Exercise 2: Remove Duplicate


let chars = ['A', 'B', 'A', 'C', 'B'];

function removeDuplicate(array) {
    
    uniqueArray = array.filter((element, index) => {
        return array.indexOf(element) === index;
    });

    return uniqueArray
}

console.log(removeDuplicate(chars))

// Exercise 3: Remove Certain Values

function removeCertainValue(array) {
    filtered = array.filter(element => element)

    return filtered
}

console.log(removeCertainValue([NaN, 0, 15, false, -22, '',undefined, 47, null]))

// Exercise 4: Repeat Please!

function repeat(word, count) {
    return count < 1 ? '': new Array(count + 1).join(word)
}

console.log(repeat("Ha!", 5))

// Exercise 5: Turtle & Rabbit

const startLine = '     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';

function printRace(startLine, characters) {
    console.log(startLine);
    characters.forEach(character => {
        console.log('       ' + character);
    });
}

const characters = ['🐢', '🐇']

printRace(startLine, characters);

