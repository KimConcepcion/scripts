# To the extent possible under law, the author(s) have dedicated all 
# copyright and related and neighboring rights to this software to the 
# public domain worldwide. This software is distributed without any warranty. 
# You should have received a copy of the CC0 Public Domain Dedication along 
# with this software. 
# If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 

# /etc/bash.bashrc: executed by bash(1) for interactive shells.

# System-wide bashrc file

# Check that we haven't already been sourced.
([[ -z ${CYG_SYS_BASHRC} ]] && CYG_SYS_BASHRC="1") || return

# If not running interactively, don't do anything
[[ "$-" != *i* ]] && return

# Set a default prompt of: user@host, MSYSTEM variable, and current_directory
#PS1='\[\e]0;\w\a\]\n\[\e[32m\]\u@\h \[\e[35m\]$MSYSTEM\[\e[0m\] \[\e[33m\]\w\[\e[0m\]\n\$ '

# Uncomment to use the terminal colours set in DIR_COLORS
eval "$(dircolors -b /etc/DIR_COLORS)"

# Fixup git-bash in non login env
shopt -q login_shell || . /etc/profile.d/git-prompt.sh

# Alias
alias ls='ls $LS_OPTIONS'
alias ll='ls $LS_OPTIONS -l'
alias l='ls $LS_OPTIONS -lA'
alias bbbConnect='ssh root@beagle'
alias python='winpty python.exe'

#-------------------------------------------------------------------------------------------------#
# MY STUFF
#-------------------------------------------------------------------------------------------------#

# Print Git branch beside directory name
parse_git_branch() 
{
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# User prompt \u + \w
PS1="$(tput bold)$(tput setaf 7)\u@$(tput setaf 6){\W}\[\e[91m\]@\$(parse_git_branch)$(tput sgr0)-->";
export PS1;

# Welcome screen:
echo '========================================================================'
echo '#                               .---.                                  #'
echo '#                              /     \                                 #'
echo '#                              \.@-@./                                 #'
echo '#                              /`\_/`\                                 #'
echo '#                             //  _  \\                                #'
echo '#                            | \     )|_                               #'
echo '#                           /`\_`>  <_/ \                              #'
echo '#                           \__/'-----'\__/                              #'
echo '========================================================================'
printf '# Date: %s                                          #\n' "$(date)"                        
printf '# Git user:  %s                                               #\n' "$(git config user.name)"    
printf '# Git email: %s                                 #\n' "$(git config user.email)" 
echo '========================================================================'
echo 'Welcome back sir!'
