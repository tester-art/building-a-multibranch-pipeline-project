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
            }
        }
    }
return changedFiles
}

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                def changed = getChangedFilesList().unique()

changed.each { item ->
        echo "ITEM : ${item}"
    }
                }
            }
        }
    }
}