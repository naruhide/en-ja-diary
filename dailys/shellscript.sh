#!/bin/bash -vx

function apt_system_upgrade () {
  echo -e "\n$(date "+%d-%m-%Y --- %T") --- Starting work\n"
  sudo apt-get update
  sudo apt-get -y upgrade
  sudo apt-get -y autoremove
  sudo apt-get autoclean
  echo -e "\n$(date "+%T") \t Script Terminated"
}

function git_push () {
  git add .
  read -p 'Enter commit message: ' COMMIT_MESSAGE
  git commit -m "$COMMIT_MESSAGE"
  expect -c "
  spawn git push -u origin master
  expect \"Username\" ; send \"$GIT_USERNAME\n\"
  expect \"Password\" ; send \"$GIT_ACCESS_TOKEN\n\"
  expect \"$\"
  exit 0
  "
}

# apt_system_upgrade
git_push
