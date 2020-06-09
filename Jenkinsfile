// returns a list of changed files
def detect_changes() {
    changedFiles = []
    echo "CURR BUILD : " + currentBuild
    echo "CURR BUILD CAUSE : " + currentBuild.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
    echo "CURR BUILD NUMBER : " + currentBuild.getNumber()
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
    if(build != null && build.result != 'FAILURE') {
        //Recurse now to handle in chronological order
        lastSuccessfullBuild(build.getPreviousBuild());
        //Add the build to the array
        echo "BUILD : " + build
        echo "BUILD CAUSE : " + build.getBuildCauses('org.jenkinsci.plugins.workflow.cps.replay.ReplayCause')
        echo "BUILD NUMBER : " + build.getNumber()
        for (changeLogSet in build.changeSets) { 
        for (entry in changeLogSet.getItems()) { // for each commit in the detected changes
            for (file in entry.getAffectedFiles()) {
                    echo "change set file : " + file.getPath().toString(); 
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