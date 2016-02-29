#!/bin/bash


set -v on

DEPLOYPROJECTNAME="mlab"
NEWVERSION=$(git rev-parse --short HEAD)
DEPLOYCOPY="~/DEPLOY/"
DEPLOYDEST="~/DEPLOY/mlab_deploy/"
DEPLOYFILENAME=deploy_${DEPLOYPROJECTNAME}_${NEWVERSION}.tar.gz
DEPLOYSERVER="ubuntu@site.yimu.me"


tar -zcf ../$DEPLOYFILENAME * --exclude=venv --exclude=scripts

scp -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 ../${DEPLOYFILENAME} ${DEPLOYSERVER}:${DEPLOYCOPY}
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 $DEPLOYSERVER "ls -l $DEPLOYCOPY;"
ssh -i ~/.ssh/id_rsa  -o StrictHostKeyChecking=no -p 22 $DEPLOYSERVER "$DEPLOYCOPY/remote_execute.sh $NEWVERSION $DEPLOYCOPY $DEPLOYDEST $DEPLOYPROJECTNAME $DEPLOYFILENAME;"
