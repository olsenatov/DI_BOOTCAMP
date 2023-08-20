// // simple loop

// const rowCount = 6
// let starLine = ''
// for (let i = 0; i < rowCount; i++) {
//     starLine += ' *'
//     console.log(starLine)
// }


// // nested loop

const rowCount = 6
for (let i = 0; i < rowCount; i++) {
    let starsNum = i + 1
    let starLine = ''
    for (x = 0; x < starsNum; x++) {
        starLine += " *"
    }
    console.log(starLine)
}

