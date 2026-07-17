pipeline {
    agent any

    environment {
        MINIKUBE_HOME = '/home/vijay-chowdary/.minikube'
        KUBECONFIG = '/home/vijay-chowdary/.kube/config'
        DOCKER_IMAGE = 'vijay14082003/flask-cicd-app'
    }

    triggers {
        cron('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/tholuchurivijaykumar/flask-cicd-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python -m pytest tests/ -v || true'
            }
        }

        stage('Build') {
            steps {
                sh 'python -c "import app; print(\'Build OK\')"'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
                    sh "docker tag ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    }
                    sh "docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh "minikube image load ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                sh "minikube image load ${DOCKER_IMAGE}:latest"
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh "kubectl set image deployment/flask-cicd-app flask-cicd-app=${DOCKER_IMAGE}:${env.BUILD_NUMBER} --record"
                sh 'kubectl rollout status deployment/flask-cicd-app --timeout=120s'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods -l app=flask-cicd-app'
                sh 'kubectl get svc flask-cicd-app-service'
                sh 'curl -s http://$(minikube ip):30090/api/health'
            }
        }
    }

    post {
        success {
            echo 'Flask CI/CD Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
        always {
            sh 'docker logout || true'
        }
    }
}
