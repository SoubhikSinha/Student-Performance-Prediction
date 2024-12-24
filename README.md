# Student Performance Prediction

<b>Acknowledgements</b>
---
I would like to extend my sincere thanks to  [Krish Naik](https://www.linkedin.com/in/naikkrish/) for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resources.

<br>
<br>

<b>About the Project</b>
---
This project predicts a student's **Math Score** based on the following inputs:

-   **Gender**
-   **Race/Ethnicity**
-   **Parental Level of Education**
-   **Lunch Type** (e.g., free/reduced or standard)
-   **Test Preparation Course** (completed or not)
-   **Writing Score** (out of 100)
-   **Reading Score** (out of 100)

<br>
<br>

<b>Purpose</b>
---
The primary objective of building this project is to understand the structure and workflow of a machine learning project, particularly in a manner that resembles **industry-level practices**. This includes organizing components such as :

-   **Artifacts** : To store model files, datasets, and results.
-   **Logs** : To track the progress and performance of the model during development and deployment.
-   **Source Code (src)** : For implementing the logic, including data preprocessing, model training, and prediction.

<br>
<br>

<b>Key Features</b>
---
-   Predicts a student's performance in Mathematics based on multiple input factors.
-   Demonstrates the deployment of a machine learning model using Flask for a simple, user-friendly web application.
-   Offers insights into integrating various project components like logging, modular code structure, and prediction models.

<br>
<br>

<b>Motivation</b>
---
This project serves as an educational tool for beginners and developers aiming to :

-   Learn how to build, structure, and deploy a machine learning project.
-   Understand the process of integrating frontend and backend components in real-world applications.
-   Gain experience with Flask, logging, and ML pipeline organization.

<br>
<br>

<b>How to Run the Code</b>
---
1. Clone the repository to your local machine using this command ▶️ `git clone https://github.com/SoubhikSinha/Student-Performance-Prediction.git`
2. Navigate to the project directory and create a virtual environment using Conda ▶️ `conda create --prefix ./venv python=3.12 -y`
3. Activate the virtual environment ▶️ `conda activate venv/`
4. Go to `requirements.txt` :
	- Uncomment ▶️ `-e .`
5. Install all the required libraries ▶️ `pip install - requirements.txt`
6. Run this command from the CMD / Terminal to build the project ▶️ `python setup.py`
7. After building the project, revert the changes to `requirements.txt` by commenting the line `-e .`
8. Start the Flask server ▶️ `python application.py`
9. Open your browser and navigate to ▶️ `localhost:5000/predictdata`<br>
*(Note: The port number might differ based on your system configuration.)*
10. Play around with the API by providing input data and observing predictions.
11. Once you're done, go back to the CMD / Terminal and press `Ctrl+C` to stop the server.

<br>
<br>

<b>How to Use</b>
---
1.  Input the required fields in the web application.
2.  Click *"Predict your Maths Score"*.
3.  The predicted score will be displayed on the screen.
