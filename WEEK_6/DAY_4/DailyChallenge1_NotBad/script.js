const sentence = 'The movie is not that bad to watch it together with the family'
let sentenceArray = sentence.split(' ')
console.log(sentenceArray)

let wordNot = ' '
let wordBad = ' '
for (let i = 0; i < sentenceArray.length; i++) {
    
    if (sentenceArray[i] === 'not') {
        wordNot += 'not'
    }
    else if (sentenceArray[i] === 'bad') {
        wordBad += ' bad'
    }
}
console.log(wordNot, wordBad) 

const indexNot = sentenceArray.indexOf('not')
const indexBad = sentenceArray.indexOf('bad')

if (indexNot < indexBad) {
    sentenceArray.splice(indexNot, (indexBad - indexNot) + 1 , 'good')
    goodSentence = sentenceArray.join(' ')
    console.log(goodSentence)  
}
else {
    console.log(sentence)
}
