pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python manage.py collectstatic --noinput'
      }
    }

    stage('Database Migration') {
      steps {
        // Apply database migrations
        sh 'python manage.py migrate'
      }
    }

    stage('Test') {
      steps {
        sh 'python manage.py test'
      }
    }

    stage('Deploy') {
      steps {
        // Deploy the Django project
        // Add your deployment steps here
      }
    }
  }
}