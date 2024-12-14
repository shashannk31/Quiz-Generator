🧠 Quiz App: Test Your Knowledge!
Welcome to the Quiz App, a fun and interactive way to challenge your knowledge on various topics! This application is designed to provide a seamless and engaging quiz experience for users, featuring a clean interface, instant feedback, and detailed results. Whether you're looking to learn, teach, or just pass some time, this app has you covered!

🚀 Features
Dynamic Quiz Generation: Questions are loaded dynamically from a CSV file, ensuring flexibility and ease of customization.
Beautiful UI/UX: Enjoy a sleek and responsive interface designed with user experience in mind.
Personalized Feedback: Get detailed insights into your answers with color-coded highlights for correct and incorrect options.
Interactive Results Page: Review your responses with explanations for every question.
Mobile Friendly: Fully responsive design for an optimal experience on all devices.
📋 How It Works
Homepage: Start your quiz journey by clicking the Start Quiz button.
Quiz Page: Answer each question by selecting one of the multiple-choice options.
Results Page: Review your performance with detailed feedback, including the correct answer for each question.
🛠️ Installation
Follow these steps to get the project running on your local machine:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/quiz-app.git
cd quiz-app
Install Dependencies: Ensure you have Python installed, then run:

bash
Copy code
pip install -r requirements.txt
Set Up the Database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Server:

bash
Copy code
python manage.py runserver
Access the App: Open your browser and go to http://127.0.0.1:8000.

🧑‍💻 Customizing the Questions
To add or modify quiz questions:

Open the questions.csv file located in the project folder.
Use the following format for the columns:
css
Copy code
text, A, B, C, D, correct_option
Save the file, and the new questions will automatically load in the app.
🎨 Screenshots
1. Homepage

2. Quiz Page

3. Results Page
