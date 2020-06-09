// returns a list of changed files
def detect_changes() {
    changedFiles = []
    isReplay = currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
    if (isReplay.size() != 0) {
        cbuildno = currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause').shortDescription[0]
        lastBuildID = cbuildno.tokenize("#")[1].toInteger()
        changedFiles = lastSuccessfullBuild(currentBuild.getPreviousBuild(), lastBuildID)
    }
    else {
        changedFiles = get_changes(currentBuild)
    }
    
    for (f in changedFiles.unique()) {
        dirname = sh (
            script: 'dirname ' + f,
            returnStdout: true
        ).trim()
        if (fileExists(f)&&dirname.equals("deployment")) {
            sh "mv " + f + " deploy_tmp"
        }
    }
}

def get_changes(build) {
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

def lastSuccessfullBuild(build, bno) {
    changedFiles = []
    if (build != null) {
        isReplay = build.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
      
        if (isReplay.size() != 0 && build.getNumber() == bno) {
            cbuildno = build.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause').shortDescription[0]
            lastBuildID = cbuildno.tokenize("#")[1].toInteger()
            bno = lastBuildID
        }

        if (build.getNumber() == bno && isReplay.size() == 0) {
            changedFiles = get_changes(build)
            return changedFiles
        }
        lastSuccessfullBuild(build.getPreviousBuild(), bno);
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