let sentence = prompt("Please enter the sentence")
let wordNot = sentence.indexOf("not")
let wordBad = sentence.indexOf("bad")

if (wordBad > wordNot) {
    sentence = sentence.slice(wordNot, wordBad)

    console.log(sentence)
}
else {
    console.log(sentence)
}