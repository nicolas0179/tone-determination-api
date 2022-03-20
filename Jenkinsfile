pipeline {
    environment {
        IMAGE_NAME = "tone-determination-api"
        registryCredentialsId = 'docker-jenkins'
        dockerImage = ''
    }
    agent any

    stages {
        stage ('Checkout'){
            steps {
                checkout scm
            }
        }

        stage ('Build') {
            steps{
                script {
                  dockerImage = docker.build IMAGE_NAME
                }
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://vps-20c3d535.vps.ovh.net/v2', registryCredentialsId) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Remove Unused docker image') {
              steps{
                sh "docker rmi $IMAGE_NAME:$BUILD_NUMBER"
                 sh "docker rmi $IMAGE_NAME:latest"

              }
        }
    }
}
