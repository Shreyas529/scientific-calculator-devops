pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shreyas529/scientific-calculator-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t terminator29/scientific-calculator:latest .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push terminator29/scientific-calculator:latest'
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i ansible/hosts.ini ansible/deploy.yml'
            }
        }
    }

    post {
        success {
            emailext (
                to: 'shreyasarun23@gmail.com',
                subject: "✅ Jenkins Job '${env.JOB_NAME}' Success",
                body: """<p>Good news!</p>
                <p>The Jenkins job <b>${env.JOB_NAME}</b> completed successfully.</p>
                <p>Build number: ${env.BUILD_NUMBER}</p>
                <p>Git commit: ${env.GIT_COMMIT}</p>
                <p>See details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                to: 'shreyasarun23@gmail.com',
                subject: "❌ Jenkins Job '${env.JOB_NAME}' Failed",
                body: """<p>Uh oh!</p>
                <p>The Jenkins job <b>${env.JOB_NAME}</b> failed.</p>
                <p>Build number: ${env.BUILD_NUMBER}</p>
                <p>See details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                mimeType: 'text/html'
            )
        }
    }
}
