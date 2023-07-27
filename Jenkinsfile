node {
    stage('Build') {
        checkout scm
        try {
            sh "docker volume rm langchain-test-pip-cache"
        }
        catch (Exception e) { }
        sh "docker build -t p0rt23/langchain-test ."
    }
}
