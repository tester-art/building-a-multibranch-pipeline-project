// returns a list of changed files
def getChangedFilesList() {
    changedFiles = []
    for (changeLogSet in currentBuild.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                //changedFiles.add(file.getPath()) // add changed file to list
                echo "type : " + file.getEditType().getName()
                bool = file.getPath().toString()
                echo "BOO " + bool
                if(file.getEditType().getName().equals("add")||file.getEditType().getName().equals("edit")) {
                changedFiles.add(bool)
                }
                if (bool.contains('J')) {
                    echo "YES"
                }
                
            }
        }
    }
    
    for (i in changedFiles.unique()) {
    dirname = sh (
        script: 'dirname ' + i,
        returnStdout: true
    ).trim()
    echo "DNAME : " + dirname
        echo "i2p : " + i
        if (fileExists(i)) {
    echo 'Yess'
    sh "mv " + i + " deploy_tmp"
} else {
    echo 'Noo'
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
                getChangedFilesList()
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