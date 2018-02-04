alias 7znew '7z a -t7z -m0=lzma2 -mx=9 -mfb=64 -md=32m -ms=on'
alias gitcam 'git commit -am'
alias aria 'aria2c -c -k5M -s32 -j32 -x16'
alias gpom 'git push origin master'
alias ytdl-audio "youtube-dl -f 'bestaudio/best' -x -o '%(title)s.%(ext)s'"
alias ytdl-vid "youtube-dl -f 'bestvideo+bestaudio/best' -o '%(title)s.%(ext)s'"
alias ytdl-pla "youtube-dl -f 'bestaudio/best' -x -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'"
alias brewup "brew update; brew update; brew upgrade; brew prune; brew cleanup; brew doctor"
alias vim "nvim"
