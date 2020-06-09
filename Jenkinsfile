// returns a list of changed files
def detect_changes() {
    changedFiles = []
    echo "CURR BUILD CAUSE : " + currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
    echo "CURR BUILD NUMBER : " + currentBuild.getNumber()
    echo "CURR BUILD RESULT : " + currentBuild.result
    isReplay = currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
    if (isReplay.size() != 0) {
         echo "IT IS A REPLAY"
        cbuildno = currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause').shortDescription[0]
        echo "rep num : " + cbuildno.tokenize("#")[1]
        lastBuildID = cbuildno.tokenize("#")[1]
        if (lastBuildID.toInteger() == 336) {
            echo "OUI!"
        }
    }
    else {
        echo "NOT A REPLAY"
    }
    for (changeLogSet in currentBuild.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                    if(file.getEditType().getName().equals("add")||file.getEditType().getName().equals("edit")) {
                        changedFiles.add(file.getPath().toString()) // add changed file to list
                    }    
            }
        }
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


def lastSuccessfullBuild(build) {
    passedBuilds = []
    if(build != null) {
        //Recurse now to handle in chronological order
        lastSuccessfullBuild(build.getPreviousBuild());
        //Add the build to the array
        echo "BUILD CAUSE : " + build.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
        echo "BUILD NUMBER : " + build.getNumber()
        echo "BUILD RESULT : " + build.result
        for (changeLogSet in build.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                    echo "CHANGES : " + file.getPath().toString(); 
            }
        }
    }
        passedBuilds.add(build);
    }
 }

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    lastSuccessfullBuild(currentBuild.getPreviousBuild());
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