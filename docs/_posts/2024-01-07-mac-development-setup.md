---
layout: post
title: My Mac Development Setup
permalink: /my-mac-development-setup-2024/
date:   2024-01-07 13:50:00 -0300
categories: ["mac", "dev-environment"]
tags: ["mac", "dev-environment"]
---

In 2016 I had my first experience working with a mac, it still had the [infamous touch bar](https://www.reddit.com/r/apple/comments/utkr3o/why_do_people_hate_the_touchbar/), but i was wonderstruck with how nice to use the system was, I always liked linux, but felt that the "user experience" was lacking, even for developers _( we also can have nice things)_. At that time i was not willing to pay for a mac, but then i got a job that provided me with one, i was hooked. Now as a proud owner of a [macbook pro M1](https://support.apple.com/kb/SP858?locale=en_US), i decided to write down my setup, so i can easily replicate it in the future (and if anyone else is interested on it).


### Macbook Specifications
+ Screen 16 inch
+ Processor Apple M1 Max - 10 (8 performance and 2 efficiency)
+ 32GB of RAM
+ 512 GB SSD storage
+ macOS Sonoma


### Brew
startin with the default choice of package manager
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
```

### Sdk Man
If you do any kind of java/kotlin develpment, this is a must have to manage your versions.

```bash
curl -s "https://get.sdkman.io" | bash
```


### Oh My Zsh
Install Oh My Zsh
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
omz update
source ~/.zshrc
```

Additional setup
```bash
brew install starship
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
brew tap homebrew/cask-fonts
brew install --cask font-hack-nerd-font
```

Open iTerm2 and update the font to `font-hack-nerd-font`.

### Update .zshrc file

include the configuration as follows ( already adding some aliases)
```bash
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

autoload -U compinit && compinit

source ./antigen.zsh
antigen use oh-my-zsh

antigen bundle zsh-users/zsh-completions
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-syntax-highlighting

antigen apply


plugins=(
    git
)

source $ZSH/oh-my-zsh.sh

# User configuration
alias code="code --profile=\"victorl2\""
alias ip="ipconfig getifaddr en0" # get machine's ip address
alias sshhome="cd ~/.ssh" # navigate to global ssh directory
alias sshconfig="code --profile=\"victorl2\" ~/.ssh/config && clear" # edit global ssh configuration
alias config="code --profile=\"victorl2\" ~/.zshrc && clear" # edit zsh configuration
alias gcc="gcc-13"
alias g++="g++-13"

eval "$(starship init zsh)"
#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
```

### Programming languages

Go
```bash
brew install go
```

C/C++
```bash
brew install gcc
```

Python _( i need to get around to use pyenv to manage versions)_
```bash
brew install python
```

Java 21
```bash
sdk install java 21.0.1-amzn
```

Kotlin 1.9
```bash
sdk install kotlin 1.9.21
```

Ruby _( only for [static site generation](https://jekyllrb.com/), not really used )_
```bash
brew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
gem install bundler:2.3.26
gem update 
```

### General Apps
installing basic apps/tools
```bash
brew install --cask \
    gh
    bitwarden \
    google-chrome  \
    firefox \
    tor \
    iterm2 \
    visual-studio-code \
    docker \
    slack \
    rectangle \
    figma \  
    discord \
    vlc
```

### Git

```bash
git config --global user.name "Your Name"
git config --global user.email "you@your-domain.com"
git config --global init.defaultBranch main
```

### VSCODE
Go to vscode and import the profile `victorl2` with the shortcut `⌘ + P` and `>profile: import profile` from this [github gist](https://gist.github.com/victorl2/d473de94d86e2ea2aafcc26a0353fcc3)


