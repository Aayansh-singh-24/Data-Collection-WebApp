# Flask Application with CI/CD & Docker Deployment  

A production-style Flask web application deployed using Docker, GitHub Actions (CI/CD), and AWS EC2.

This project demonstrates an automated build, push, and deployment pipeline using modern DevOps practices.

---


## 🌐 Live Application  

👉 Access the deployed app:  
http://44.200.207.38:5000/login?next=%2F  

> ⚠️ Note: This app runs on HTTP (no HTTPS), so browsers may show a "Not Secure" warning.

---

## 📌 Features  

- 🐳 Dockerized Flask application  
- 🔁 Automated CI/CD pipeline using GitHub Actions  
- 📦 Docker image pushed to Docker Hub  
- ☁️ Auto-deployment on AWS EC2 via SSH  
- 🏷️ Versioned Docker images using commit SHA  
- 🚀 One-push deployment (push → live app)

---


## 🛠️ Tech Stack  

- Backend: Flask (Python)  
- Containerization: Docker  
- CI/CD: GitHub Actions  
- Cloud: AWS EC2  
- Registry: Docker Hub  

---


## ⚙️ CI/CD Workflow  

The pipeline is triggered whenever code is pushed to the `main` branch.

### 🔄 Steps:

1. Checkout Code  
2. Login to Docker Hub  
3. Build Docker Image  
   - Tagged with:
     - latest  
     - commit SHA  
4. Push Image to Docker Hub  
5. SSH into EC2  
6. Pull Latest Image  
7. Stop Old Container  
8. Run New Container  

---


## 📂 Project Structure  

![Project Structure](https://github.com/user-attachments/assets/1f156ef9-1cbc-4b25-a0fe-52738b22d76e)

---


## 💡 Improvements (Future Scope)

- Add Nginx reverse proxy  
- Enable HTTPS (Let’s Encrypt)  
- Use Docker Compose for multi-container setup  
- Add monitoring (Prometheus + Grafana)  
- Implement zero-downtime deployment  

---

## 💣 One-Line Summary  

Automated CI/CD pipeline that builds a Dockerized Flask app, pushes it to Docker Hub, and deploys it on AWS EC2 using GitHub Actions.