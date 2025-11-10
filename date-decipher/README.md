# Date Decipher

Welcome to Date Decipher, a web-based chat interface designed to recreate the experience of flirting by passing a note to your crush. This unique chat application captures real-time facial expressions to assess interest, enhancing interactions with dynamic feedback.

## Video Walkthrough

Watch this video walkthrough (https://youtu.be/3Ip_VW0s-7o?si=5SVgwdZiQJDEedpV) to see Date Decipher in action and understand how it works from a user's perspective.


## Features

- **User Authentication**: Includes functionalities for user registration, login, and password reset.
- **Live Chat Interface**: Simulates passing a note to your crush with pre-defined flirty chats.
- **Emotion Detection**: Utilizes Google Cloud Vision API to analyze facial expressions and represent them with emojis.
- **Feedback System**: Evaluates the emojis to determine if your crush is likely to be interested and provides feedback.
- **Privacy Focused**: Ensures privacy by clearing feedback after viewing and redirecting users to the home page.

## Getting Started

Follow these instructions to set up and run Date Decipher on your local machine for development and testing purposes.

### Prerequisites

Before you start, ensure you have Python 3.8 or higher installed along with pip. You'll also need a Google Cloud Vision API key for emotion detection features.

### Installation Steps

1. **Download and Extract the Project**:
   - Download the `date-decipher.zip` file and extract its contents into your preferred directory.

2. **Environment Setup**:
   - Open the Date Decipher folder in a code editor that supports integrated terminals, such as VS Code.
   - Right-click and choose "Open in Integrated Terminal".

3. **Install Dependencies**:
   ```bash
   pip install Flask requests google-cloud-vision


4. **Configure Google Cloud Vision API**:
    Obtain an API key from the Google Cloud Console.

#### Running the Application

1. **Launch the Server**:
    ```bash
    flask run
    ```
    This command starts the server on your local machine.

2. **Access the Application**:
    Use the HTTP link shown in the terminal to open Date Decipher in a web browser.

3. **Interaction Guide**:
    - Log in or register to initiate the chat.
    - Conduct the chat session. Once completed, a 'Get Feedback' button will appear.
    - Click 'Get Feedback' to see the analysis based on your crush's reactions.
    - Feedback will automatically clear, redirecting you back for privacy.

##### Troubleshooting

- **Problem**: Application does not start.
  **Solution**: Ensure all dependencies are installed and the environment variable for the Google Cloud API key is set.

- **Problem**: Emotion detection is not working.
  **Solution**: Verify that the Google Cloud Vision API key is valid and has not expired. Check the console for any error messages that might indicate what went wrong.

##### Acknowledgments

- **Google Cloud Vision**: Special thanks to Google Cloud Vision for providing the facial recognition technology that powers the emotion detection capabilities of our application.
- **Flask Community**: Appreciation to the Flask community for the robust web framework that forms the backbone of our application.
- **Open-Source Contributors**: Thanks to all open-source contributors whose tools were utilized in this project, enhancing its functionality and reliability.
- **Project Inspiration**: Inspired by [Valentine](https://valentine.mewtru.com/), this project aims to capture the magic of the moment you ask someone to be your Valentine using an engaging animation
- **CS50 Duck and OpenAI's ChatGPT**: Gratitude to CS50 Duck and OpenAI's ChatGPT for their assistance in debugging and refining the project.


