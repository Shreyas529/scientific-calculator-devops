pipeline {
    agent any

    environment {
        DOCKERHUB_CRED = credentials('dockerhub-creds') // Docker Hub credentials stored in Jenkins
    }

    stages {

        stage('Checkout') {
            steps {
                // Checkout your main branch from GitHub
                git branch: 'main', 
                    url: 'https://github.com/Shreyas529/scientific-calculator-devops.git', 
                    credentialsId: 'github-creds'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Add local bin to PATH so pytest is found
                sh 'export PATH=$PATH:/var/lib/jenkins/.local/bin && pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t shreyas529/scientific-calculator:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                // Push Docker image to Docker Hub using stored credentials
                withDockerRegistry([credentialsId: 'dockerhub-creds', url: '']) {
                    sh 'docker push shreyas529/scientific-calculator:latest'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                // Run your Ansible playbook to deploy container
                sh 'ansible-playbook -i ansible/hosts.ini ansible/deploy.yml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output for errors.'
        }
    }
}
