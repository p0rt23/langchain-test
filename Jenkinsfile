node {
    stage('Build') {
        checkout scm
        sh "docker volume rm langchain-test-pip-cache"
        sh "docker build -t p0rt23/langchain-test ."
    }
}
