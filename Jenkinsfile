// returns a list of changed files
def detect_changes() {
    changedFiles = []
    isReplay = currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
    if (isReplay.size()) {
        lastBuildNo = isReplay.shortDescription[0].tokenize("#")[1].toInteger()
        changedFiles = getOriginalBuild(currentBuild.getPreviousBuild(), lastBuildNo)
    }
    else {
        changedFiles = fetchChangeset(currentBuild)
    }
    
    for (f in changedFiles.unique()) {
        dirname = sh (
            script: 'dirname ' + f,
            returnStdout: true
        ).trim()
        if (fileExists(f) && dirname.equals("deployment")) {
            sh "mv " + f + " deploy_tmp"
        }
    }
}

def fetchChangeset(build) {
    changedFiles = []
    for (changeLogSet in build.changeSets) { 
        for (entry in changeLogSet.getItems()) {
            for (file in entry.getAffectedFiles()) {
                    if(file.getEditType().getName().equals("add")||file.getEditType().getName().equals("edit")) {
                        changedFiles.add(file.getPath().toString())
                    }    
            }
        }
    }
    return changedFiles
}

def getOriginalBuild(build, buildNo) {
    if (build != null) {
        isReplay = build.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
      
        if (build.getNumber() == buildNo) {
            if (isReplay.size()) {
                lastBuildID = isReplay.shortDescription[0].tokenize("#")[1].toInteger()
                buildNo = lastBuildID
            }
            else {
                return fetchChangeset(build)
            }
        }
        getOriginalBuild(build.getPreviousBuild(), buildNo);
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