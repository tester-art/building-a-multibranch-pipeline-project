// returns a list of changed files
@NonCPS
String getChangedFilesList() {

    sh 'mkdir -p deploy_tmp'
    for (changeLogSet in currentBuild.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                changedFiles.add(file.getPath()) // add changed file to list
                echo "type : " + file.getEditType().getName()
                sh 'mv file.getPath() deploy_tmp'
            }
        }
    }

}

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello world!"'
                echo getChangedFilesList()
                sh 'ls deploy_tmp'
            }
        }
    }
}