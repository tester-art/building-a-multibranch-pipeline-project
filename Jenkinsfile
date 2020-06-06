// returns a list of changed files
@NonCPS
def getChangedFilesList() {

    changedFiles = []
    for (changeLogSet in currentBuild.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                changedFiles.add(file.getPath()) // add changed file to list
                echo "type : " + file.getEditType().getName()
            }
        }
    }
    sh 'mkdir deploy_tmp'
    changedFiles.each { item ->
        sh "mv ${item} deploy_tmp"
    }

}

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello world!"'
                getChangedFilesList()
                sh 'ls deploy_tmp'
            }
        }
    }
}