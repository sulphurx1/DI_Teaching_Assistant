// Exercise 1: Colors

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

for (let i=0; i < colors.length; i++) {
    console.log(`${i + 1}# choice is ${colors[i]}`);
}

if (colors.includes("Violet")) {
    console.log("Yeah");
}
else {
    console.log("No...");
}

// Exercise 2: Colors #2 

const colors1 = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

for (let j=0; j < colors1.length; j++) {
    if (j=0 && j < 3) {
        for (let z=1; z < ordinal.length; z++) {
            console.log(`${j+1}${ordinal[z]} choice is ${colors1[j]}`)
        }
    }
    else {
        console.log(`${j+1}${ordinal[0]} choice is ${colors1[j]}`)
    }
    

    // if(j == 0) {
    //     console.log(`${j+1}${ordinal[1]} choice is ${colors1[j]}`)
    // }
    // else if(j == 1) {
    //     console.log(`${j+1}${ordinal[2]} choice is ${colors1[j]}`)
    // }
    // else if(j == 2) {
    //     console.log(`${j+1}${ordinal[3]} choice is ${colors1[j]}`)
    // }
    // else {
    //     console.log(`${j+1}${ordinal[0]} choice is ${colors1[j]}`)
    // }
}

// Exercise 3: Analyzing

// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);

// ------2------
const country = "USA";
console.log([...country]);

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);

// Exercise 4: Employees

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

const welcomeStudents = users.map((name) => "Welcome " + name.firstName);

console.log(welcomeStudents);

const onlyFullStack = users.filter((role) => role.role == 'Full Stack Resident')

console.log(onlyFullStack)

const onlyLast = onlyFullStack.map((ln) => ln.lastName)

console.log(onlyLast)

// Exercise 5: Star Wars

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

sentence = epic.reduce((accumulator, currentValue) => accumulator + " " + currentValue)

console.log(sentence)

// Exercise 6: Employees #2

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];


const studentPassed = students.filter((passed) => passed.isPassed == true)

console.log(studentPassed)

studentPassed.forEach(x => {
    console.log(`Good Job ${x.name}, you passed the course in ${x.course}`)
})

