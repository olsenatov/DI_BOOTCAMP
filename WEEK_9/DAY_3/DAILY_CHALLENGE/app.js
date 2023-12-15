const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' },
    { emoji: '❤️', name: 'Heart'},
    { emoji: '👍', name: 'Thumbs Up' }
  ];


//random emoji
function getRandomEmoji() {
    const randomIndex = Math.floor(Math.random() * emojis.length);
    const correctEmoji = emojis[randomIndex];
    const distract = getDistract(correctEmoji);
    return { correctEmoji, distract };
}

//disctract
function getDistract(correctEmoji) {
    const disctractors = [];
    while (disctractors.length < 3) {
        const randomIndex = Math.floor(Math.random() * emojis.length);
        const emoji = emojis[randomIndex];
        if (emoji !== correctEmoji && !disctractors.includes(emoji.name)) {
            disctractors.push(emoji.name);
        }
    }
    return disctractors;
}

//form submission and fetch
const form = document.getElementById('emoji-guess-form');
const emojiDisplay = document.getElementById('emoji-display');
const optionsList = document.getElementById('options');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const guess = formData.get('guess');
    const response = await fetch('/check-guess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ guess }),
    });
    const data = await response.json();

    console.log(data.feedback);
    console.log(`Your score: ${data.score}`);
    loadNewEmoji();
  });

//new emojis
function loadNewEmoji() {
    const { correctEmoji, disctractors } = getRandomEmoji();
    emojiDisplay.textContent = correctEmoji;
    optionsList.innerHTML = '';
    const options = [correctEmoji.name, ...distractors];
    options.sort(() => Math.randon() - 0.5);
    options.forEach((option) => {
        const li = document.createElement('li');
        li.textContent = option;
        optionsList.appendChild(li);
    });
}

loadNewEmoji();

//checking guess and update score
app.post('/check-guess', (req, res) => {
    const { guess } = req.body;
    const { correctEmoji } = getRandomEmoji();
    if (guess === correctEmoji.name) {
      res.json({ feedback: 'Correct!', score: 1 });
    } else {

      res.json({ feedback: 'Incorrect. Try again.', score: 0 });
    }
  });

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
  