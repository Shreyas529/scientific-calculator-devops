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
                sh 'ansible-playbook ansible/deploy.yml'
            }
        }
    }

    post {
        success {
            mail to: 'shreyasarun23@gmail.com',
                subject: "Build Success",
                body: "Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} succeeded"
        }

        failure {
            mail to: 'shreyasarun23@gmail.com',
                subject: "Build Failed",
                body: "Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} failed. Please check the Jenkins console output for details."
        }
    }
}
