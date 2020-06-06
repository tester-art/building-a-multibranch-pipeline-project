// returns a list of changed files
@NonCPS
def getChangedFilesList() {

                sh (
        script: 'mkdir -p deploy_tmp',
        returnStdout: true
    )
    for (changeLogSet in currentBuild.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                changedFiles.add(file.getPath()) // add changed file to list
                echo "type : " + file.getEditType().getName()
                sh (
        script: 'mv ' + file.getPath() + ' deploy_tmp',
        returnStdout: true
    )
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
                getChangedFilesList()
                sh 'ls'
            }
        }
    }
}