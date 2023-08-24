// Exercise 1: Find The Numbers Divisible By 23

function displayNumbersDivisible(x) {
    array = []
    let sum = 0;

    for(i=0; i<=500; i++) {
        if(i%x == 0) {
            array.push(i);
        }
    }

    array.forEach(number => {
        sum += number;
    })

    console.log(`Outcome: ${array}\nSum: ${sum}`)
}

displayNumbersDivisible(23)

// Exercise 2: Shopping List

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = ["banana", "orange", "apple"]

function adjustStock(item) {
    stock[item] -= 1
}

function myBill(shoppingList) {
    let total = 0;
    for(let item of shoppingList) {
        if(stock[item] > 0) {
            total += prices[item]
            adjustStock(item)

        }
    }

    return total
}

console.log(myBill(shoppingList))

// Exercise 3: What's In My Wallet
 let worth = [0.25, 0.10, 0.05, 0.01]
 let sum = 0;

function changeEnough(itemPrice, amountOfChange) {
    
    for (let i=0; i < amountOfChange.length; i++) {
        sum += Number(amountOfChange[i]) * Number(worth[i]);
    }

    if (sum => itemPrice) {
        return true;
    }
    else {
        return false;
    }

}

console.log(changeEnough(4.25, [25, 20, 5, 0]))
console.log(changeEnough([2, 100, 0, 0], 14.11));

// Exercise 4: Vacations Costs

function hotelCost() {

    let numberOfNights = prompt("How many nights would you stay");

    if (isNaN(parseInt(numberOfNights))) {
        let numberOfNights = prompt("How many nights would you stay");
    }
    else {
        totalPrice = 140 * parseInt(numberOfNights);
    }

    return `Total Price: $` + totalPrice;
}

function planeCost() {

    let london = 183;
    let paris = 220;
    let others = 300;

    let total = 0;

    let destination = prompt("What is your destination ?");

    if (!isNaN(destination)) {
        let destination = prompt("What is your destination ?");
    }

    if(destination.toLowerCase() == "london") {
        total = london;
    }
    else if(destination.toLowerCase() == "paris") {
        total = paris;
    }
    else {
        total = others;
    }

    return `Total Plane Cost: $` + total;
}

function rentalCarCost() {

    let rentalCost = 40;
    let total = 0;

    let rentalDays = prompt("How many days would you like to rent the car ?");

    if(isNaN(rentalDays)) {
        let rentalDays = prompt("How many days would you like to rent the car ?");
    }

    if(parseInt(rentalDays) > 10) {
        total = rental * parseInt(rentalDays);
    }
    else {
        total = rental * parseInt(rentalDays);
    }

    return `Total Cost for car rental: $` + total;
 
}

function totalVacationCost() {
    
    let x = hotelCost();
    let y = planeCost();
    let z = rentalCarCost();

    return `The car cost: $` + z + `, the hotal cost: $` + x + `, the plane ticket cost: $` + y;
}

totalVacationCost()