# Higher or Lower Game

A simple web-based higher or lower game built with Flask. Players guess a randomly selected number between 0 and 9. Feedback is provided for each guess, indicating whether the guess was too high, too low, or correct. The game showcases basic server-side logic, routing, and dynamic content generation in Flask.

## Features

- **Instant Feedback**: Provides immediate feedback on whether your guess is too high, too low, or correct.
- **Visual Cues**: Displays a fun GIF image based on the outcome of your guess.
- **Simple Interaction**: Users interact with the game by modifying the URL to submit their guesses.

## How to Play

1. **Start the Game**: Navigate to the root URL (`/`). You will be prompted to pick a number between 0 and 9.
2. **Make a Guess**: Add your guess to the end of the URL (e.g., `/5`) and press Enter.
3. **Read the Feedback**: The application will tell you if your guess is too high, too low, or correct, along with displaying a corresponding GIF.
4. **Guess Again**: Adjust your guess based on the feedback and try again by modifying the URL.

## How to Run Locally

To run the Higher or Lower Game on your local machine, follow these steps:

1. **Clone or Download This Repository**

2. **Ensure Python and Flask Are Installed**

   You need Python installed on your computer. Flask can be installed using pip if you haven't installed it yet:

   ```bash
   pip install Flask
