import chalk from 'chalk';

function displayColor(word1, word2, word3) {
    const colorfulM = chalk.bold.blue(word1) + chalk.bold.yellow(word2) + chalk.bold.green(word3);
    console.log(colorfulM);
};

export default displayColor