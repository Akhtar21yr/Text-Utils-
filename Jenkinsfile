pipeline {
    agent {
        node {
            label 'development'
        }
    }

    stages {
        stage('code') {
            steps {
                git url: "https://github.com/Akhtar21yr/Text-Utils-.git", branch: "main"
            }
        }
        stage('build & test') {
            steps {
                sh "docker build -t text-app:v1 ."
            }
        }
        stage('push to docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerCred', passwordVariable: 'dPass', usernameVariable: 'dUser')]) {
                    sh 'echo $dPass | docker login -u $dUser --password-stdin'
                    sh 'docker tag text-app:v1 $dUser/text-app:latest'
                    sh 'docker push $dUser/text-app:latest'
                }
            }
        }
        stage('deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerCred', passwordVariable: 'dPass', usernameVariable: 'dUser')]) {
                    sh 'docker pull $dUser/text-app:v1'
                }
                sh "docker compose down && docker compose up -d "

            }
        }
    }
}
