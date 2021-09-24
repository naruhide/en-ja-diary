#!/bin/bash -vx
# [summary] ...

function apt_system_maintenance () {
      echo -e "\n$(date "+%d-%m-%Y --- %T") --- Starting work\n"
      sudo apt-get update
      sudo apt-get -y upgrade
      sudo apt-get -y autoremove
      sudo apt-get autoclean
      echo -e "\n$(date "+%T") \t Script Terminated"
}

function git_push () {
      # Prerequisite:
      #    echo 'export GIT_USERNAME="your_github_username"' >> ~/.bashrc
      #    echo 'export GIT_ACCESS_TOKEN="your_github_access_token"' >> ~/.bashrc
      #    Restart Bash.

      git add .
      read -p 'Enter commit message: ' COMMIT_MESSAGE
      git commit -m "$COMMIT_MESSAGE"
      expect -c "
      spawn git push
      expect \"Username\" ; send \"$GIT_USERNAME\n\"
      expect \"Password\" ; send \"$GIT_ACCESS_TOKEN\n\"
      expect \"$\"
      exit 0
      "
}

function main () {
      ### Adjust the function you want to use with comments. ###

      # apt_system_maintenance
      git_push
}

main
echo 'Done'
