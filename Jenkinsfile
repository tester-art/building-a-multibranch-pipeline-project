// returns a list of changed files
def detect_changes() {
    changedFiles = []
    for (changeLogSet in currentBuild.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                    if(file.getEditType().getName().equals("add")||file.getEditType().getName().equals("edit")) {
                        changedFiles.add(file.getPath().toString()) // add changed file to list
                    }    
            }
        }
    }
    
    for (i in changedFiles.unique()) {
        dirname = sh (
            script: 'dirname ' + i,
            returnStdout: true
        ).trim()
        if (fileExists(i)&&dirname.equals("deployment")) {
            sh "mv " + i + " deploy_tmp"
        }
    }
}

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                sh 'mkdir deploy_tmp'
                detect_changes()
                }
            }
        }
    }
    post {
        always {
            sh 'ls deploy_tmp'
            sh "rm -rf *"
        }
    }
}