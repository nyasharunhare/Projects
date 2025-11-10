document.addEventListener('DOMContentLoaded', function() {
  const video = document.getElementById('video');
  const chat = document.getElementById('chat');
  const feedbackButton = document.getElementById('feedbackButton');
  const feedbackModal = document.getElementById('feedbackModal');
  const feedbackText = document.getElementById('feedbackText');
  let messageIndex = 0;
  const messages = [
      "💌 Hey there! 😊 Ever wondered who would win in a game of mini-golf between us? 🏌️‍♂️🏌️‍♀️",
      "What do you say we find out? Loser buys ice cream! 🍦 Spoiler: it’s gonna be you.",
      "Still on the fence? Imagine this: a gorgeous day, just us, fun games, and some laughter. How can you say no to that?",
      "I promise, it'll be the highlight of your week. Why miss out on some epic memories?",
      "Here’s a little bribe... if you say yes, the first coffee is on me, and I'll even throw in my secret talent reveal! 🌟",
      "Not convinced yet? What if I said I’ve been practicing my jokes just for you? You might just laugh all day. 😄",
      "Picture this: It's just you and me, escaping the routine. A little thrill, a little chill. 🌊🍹",
      "Let's make it a date that you won't stop talking about! I’m pretty good company, I swear!",
      "Okay, how about a sweet deal? You pick the place, I plan the fun. We can even make it a bet!",
      "Trust me, I’m a fantastic date. Fun, a bit flirty, and I know the best spots in town. 🌆",
      "I'm really hoping for a 'yes' because honestly, who else will you get to tease mercilessly all afternoon?",
      "You, me, some spontaneous plans, could be the start of something new. What do you think?",
      "Alright, I'm laying it all on the line now. Say yes and let's make some unforgettable memories. 🎇",
      "Just imagine, it could be the story we laugh about for years to come. Don’t make me wait too long!",
      "So, is it a date? Because I can’t wait to see you smile when I pick you up. 😍🚗"
  ];

  feedbackButton.style.display = 'none'; // Initially hide the feedback button

  function addMessage(text, from) {
      const messageDiv = document.createElement('div');
      messageDiv.className = 'message ' + (from === 'them' ? 'from-them' : 'from-me');
      messageDiv.innerText = text;
      chat.appendChild(messageDiv);
      chat.scrollTop = chat.scrollHeight;
  }

  function sendMessage() {
      if (messageIndex < messages.length) {
          addMessage(messages[messageIndex], "them");
          setTimeout(captureImage, 3000); // Delay to simulate reading time and capturing response
      }
  }

  function captureImage() {
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      canvas.toBlob(processImage, 'image/jpeg');
  }

  function processImage(blob) {
      const formData = new FormData();
      formData.append('image', blob);
      fetch('/analyze', {
          method: 'POST',
          body: formData
      }).then(response => response.json())
        .then(data => {
            addMessage(data.emoji, 'me');
            messageIndex++;
            if (messageIndex < messages.length) {
                setTimeout(sendMessage, 1000); // Continue the conversation
            } else {
                feedbackButton.style.display = 'block'; // Show the feedback button only after all messages are processed
            }
        }).catch(error => {
            console.error('Error processing image:', error);
            addMessage('😐', 'me'); // Fallback emoji on error
            messageIndex++;
            if (messageIndex < messages.length) {
                setTimeout(sendMessage, 1000);
            } else {
                feedbackButton.style.display = 'block'; // Show the feedback button even if the last emoji fails
            }
        });
  }

  navigator.mediaDevices.getUserMedia({ video: true })
      .then(function(stream) {
          video.srcObject = stream;
          sendMessage(); // Start sending messages once the video is set up
      })
      .catch(function(error) {
          console.error("Failed to access the camera: ", error);
          chat.innerHTML = '<div>Error accessing camera: ' + error.message + '</div>';
      });

  feedbackButton.addEventListener('click', function() {
      fetch('/get_feedback')
          .then(response => response.json())
          .then(data => {
              feedbackText.innerText = data.feedback;
              feedbackModal.style.display = "block";  // Show the modal
              setTimeout(function() {
                  feedbackModal.style.display = "none";  // Hide the modal after 5 seconds
                  window.location.href = '/';  // Redirect to the home page
              }, 5000);
          })
          .catch(error => console.error('Error getting feedback:', error));
  });
});
