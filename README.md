#  Readora – Online Book Reading Platform

## Project Overview

Readora is a Flask-based online book reading platform where users can register, log in, explore books by categories, read stories, and rate books. The project provides a simple and interactive digital library experience while demonstrating modern DevSecOps practices such as cloud deployment, containerization, CI/CD automation, monitoring, logging, and security implementation.

The application is deployed on AWS cloud infrastructure and uses Docker, GitHub Actions, Nginx, CloudWatch, and Amazon RDS to create a secure and scalable platform.

---

## Features

### User Features

- User Registration
- User Login
- User Logout
- Browse Books
- Browse Categories
- Read Stories
- Rate Books
- Profile Management

### Security Features

- Password Hashing
- HTTPS Encryption
- IAM Access Control
- Secure Database Connectivity

### DevOps Features

- Docker Containerization
- GitHub Actions CI/CD Pipeline
- AWS Cloud Deployment
- CloudWatch Monitoring
- SNS Alert Notifications
- Automated Backup Strategy

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask
- SQLAlchemy

### Database

- MySQL
- Amazon RDS

### Cloud Services

- Amazon EC2
- Amazon RDS
- Amazon S3
- Amazon CloudWatch
- Amazon SNS
- AWS IAM

### DevOps Tools

- Git
- GitHub
- GitHub Actions
- Docker
- Nginx
- Gunicorn

---

## Project Architecture

User Browser

↓

Nginx Reverse Proxy

↓

Gunicorn Application Server

↓

Flask Application

↓

Amazon RDS MySQL Database

Monitoring: CloudWatch + SNS

Storage: Amazon S3

CI/CD: GitHub Actions

Containerization: Docker

---

## Project Structure

```text
readora/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── static/
│
├── templates/
│
├── instance/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── users.db
```

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/ardrabnair7-bit/readora.git

cd readora
```

### Create Virtual Environment

```bash
python -m venv venv
```

Linux

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application URL:

```text
http://localhost:5000
```

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t readora-app .
```

### Run Docker Container

```bash
docker run -d -p 5001:5000 --name readora-container readora-app
```

### Verify Running Container

```bash
docker ps
```

---

## AWS Deployment

### Infrastructure Used

- Amazon EC2
- Amazon RDS
- Amazon S3
- Amazon CloudWatch
- Amazon SNS

### Deployment Flow

1. Push code to GitHub.
2. GitHub Actions workflow runs automatically.
3. Application build is validated.
4. Docker image is created.
5. Application is deployed on EC2.
6. Gunicorn runs the Flask application.
7. Nginx acts as reverse proxy.
8. SSL secures application traffic.
9. CloudWatch monitors system health.

---

## CI/CD Pipeline

GitHub Actions is used for Continuous Integration.

### Pipeline Stages

#### Build Stage

- Checkout Source Code
- Setup Python Environment

#### Test Stage

- Verify Dependencies
- Validate Application Configuration

#### Deploy Stage

- Prepare Deployment Artifacts
- Deploy Application

Pipeline Status:

- Build Successful
- Test Successful
- Deploy Successful

---

## Monitoring and Logging

### CloudWatch Metrics

Monitored Metrics:

- CPU Utilization
- Network In
- Network Out
- Memory Usage
- Disk Usage

### CloudWatch Alarms

Configured Alarm:

- ReadoraAlarmTopic

Alarm Condition:

- CPU Utilization greater than 80%

### SNS Notifications

Amazon SNS sends alert notifications to administrators when alarm conditions are triggered.

### Log Management

CloudWatch Log Groups are used for centralized log storage and monitoring.

---

## Health Monitoring

Health Endpoint:

```text
/health
```

Response:

```text
200 OK
```

Used for:

- Uptime Monitoring
- Service Validation
- Deployment Verification

---

## Security Implementation

### Password Protection

Passwords are hashed before storage.

### HTTPS Security

SSL/TLS certificates are configured using Let's Encrypt.

### Access Control

IAM users and security groups restrict unauthorized access.

### Application Security

- Session Management
- User Authentication
- Secure Database Connectivity

---

## Backup Strategy

Database backups are stored in Amazon S3.

Backup Process:

1. Create Database Dump
2. Upload Backup to S3
3. Maintain Backup Versions
4. Restore When Required

---

## Challenges Faced

### Database Connectivity Issues

Resolved through RDS configuration and security group updates.

### Docker Deployment Issues

Resolved container networking and image build errors.

### HTTPS Configuration

Configured Nginx and SSL certificates successfully.

### Monitoring Setup

Configured CloudWatch Agent, Metrics, Alarms, and SNS notifications.

### CI/CD Workflow Setup

Implemented GitHub Actions automation for build and deployment validation.

---

## Future Enhancements

- Mobile Application
- Recommendation System
- Multi-Factor Authentication
- Advanced Search Features
- Kubernetes Deployment
- Terraform Infrastructure as Code
- Automated Security Scanning
- Load Balancing
- Auto Scaling

---

## References

### AWS Documentation

- https://docs.aws.amazon.com/ec2/
- https://docs.aws.amazon.com/rds/
- https://docs.aws.amazon.com/s3/
- https://docs.aws.amazon.com/cloudwatch/
- https://docs.aws.amazon.com/sns/

### Other Resources

- https://flask.palletsprojects.com/
- https://docs.docker.com/
- https://docs.github.com/actions
- https://nginx.org/en/docs/
- https://letsencrypt.org/docs/

---

## Author

**Ardra B Nair**

DevSecOps Capstone Project

Readora – Online Book Reading Platform

Marian College Kuttikkanam (Autonomous)

2026
