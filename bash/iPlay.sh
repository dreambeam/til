#!/bin/bash
#
# This script plays the songs from the command line
# when given the location of music folder
# Author: Bleza Takouda <dreambeam77@gmail.com>
# Copyright: Bleza Takouda, (c) 2017
# Version: 0.1
# License: GPLv2
# Description: Music player from CLI
# Run as follow:
# $ bash iPlay.sh /DIRECTORY 0
# or
# $ bash iPlay.	/DIRECTORY 1
# Arguments:
# 	 - 0, order
#	 - 1, shuffle
# ToDo:
# 1. Add flags to select ordered  or shuffled play

MUSIC_FOLDER=$1
PLAY_ORDER=$2

# Create a playlist
if [[ -f playlist.txt ]]; then
	# Get the list of mp3 file
	# ls $MUSIC_FOLDER/*.mp3 > playlist.txt
	find $MUSIC_FOLDER -iname "*.mp3" > playlist.txt
fi

tobeplayed=""
i=0

while read -r line
do
	tobeplayed[$i]="$line"
	(( i++ ))
done < playlist.txt

# Randomly select/play 1 song in the play list
#suffle_song(){
#	song=${!playlist_num[@]}
#}

play(){

	playlist_num=${#tobeplayed[@]}
	#echo $playlist_num
	while [[ $playlist_num -ne 0 ]]
	do
		if [[ $PLAY_ORDER -eq 0 ]]; then
			# selected_song
			for (( j=0; j<$playlist_num; j++ ))
				do
					selected_song=${tobeplayed[$j]}
					echo "Playing > $selected_song"
					afplay "$selected_song"
				done
		elif [[ $PLAY_ORDER -eq 1 ]]; then
			rand=$(( RANDOM%${#tobeplayed[@]} ))
			#echo $rand
			selected_song=${tobeplayed[$rand]}
			echo "Playing > $selected_song"
			afplay "$selected_song"
			# afplay -h -t 180 -d selected_song
		fi
		playlist_num=$(( playlist_num-1 ))
	done
}

play
