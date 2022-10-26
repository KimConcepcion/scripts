#!/bin/bash

# ---------- Install Docker engine on Debian ----------
# Link to docs: https://docs.docker.com/engine/install/debian/

# Uninstall old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Update apt package index
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Setup docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update apt package index
sudo apt-get update

# Install latest version
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin


# ---------- Run docker without sudo ----------
# Link to docs: https://docs.docker.com/compose/install/linux/


# ---------- Run docker without sudo ----------
# Link to docs: https://docs.docker.com/engine/install/linux-postinstall/

# Create the docker group
sudo groupadd docker

# Add user to the docker group
sudo usermod -aG docker $USER

echo "Log out to update your new docker group..."
