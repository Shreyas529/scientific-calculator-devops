pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "terminator29/scientific-calculator:latest"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "✅ SUCCESS: Scientific Calculator Pipeline",
                body: "The Jenkins pipeline completed successfully.",
                to: "shreyasarun23@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "❌ FAILURE: Scientific Calculator Pipeline",
                body: "The Jenkins pipeline failed. Check logs for details.",
                to: "shreyasarun23@gmail.com"
            )
        }
    }
}
