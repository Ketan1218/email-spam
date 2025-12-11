Email Spam Classifier (Streamlit App)
- This project is a simple machine-learning web app that classifies emails as Spam or Not Spam using a trained Naive Bayes model.
The app is built with Python, scikit-learn, Streamlit, nltk, pickle, pandas, numpy are bunch of libraries used in this project.


Features
- Predict whether an email is spam or not
- Uses TF-IDF vectorizer + trained ML model
- Runs as a lightweight Streamlit web app

Project Structure:
app.py
model.pkl
vectorizer.pkl
requirements.txt


🛠️ Installation & Setup (Local System)

1️⃣ Clone the Repository
git clone <your-repo-url>
cd <project-folder>

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py

5️⃣ Open in Browser
Streamlit will show a local URL, usually:
http://localhost:8501

============================================================================

Deploying on AWS EC2 (Short Guide)
- Launch an Ubuntu EC2 instance
- Allow inbound ports: 80 and 8501
- SSH into the instance
- Install Python & Git


Clone your GitHub repo
git clone <your-repo-url>
cd <project-folder>

Install requirements
pip install -r requirements.txt

Run Streamlit
streamlit run app.py --server.address 0.0.0.0 --server.port 8501

Open in browser:
http://<your-ec2-public-ip>:8501

============================================================================

📧 Contact

For any issues or contributions, feel free to open an issue or reach out.
