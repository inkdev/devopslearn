#!/bin/bash

#SOURCEDIR='/home/alexis/genpy/TESTFILE/*'
#TARGETDIR='/home/alexis/genpy/DESTDIR'
#LOGFILENAME='/home/alexis/genpy/logfile.log'

CONFDIR=${PWD}
source "$CONFDIR"/mover.conf

check_log() {

LOGDIR=$(dirname "${LOGFILENAME}")
touch $LOGFILENAME
}
if [[ -d $SOURCEDIR ]] && [[ -d $TARGETDIR  ]] 
	then
	check_log
else
	echo "Source or target directory does not exist"
	exit 1
fi

move_func() {
	for file in "$SOURCEDIR"/*; do
		SYSDATE=$(date +"%Y-%m-%d %H:%M:%S")
	        FILENAME=$(head -n1 $file | awk '{IFS="\t"} {print $1}')
	        FILEDATE=$(head -n1 $file | awk '{IFS="\t"} {print $2 " " $3}')
		NEWNAME="$FILENAME $FILEDATE $SYSDATE"
	        LP=$(echo $(tail -n1 $file))
		        if [[ $LP =~ [a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12} ]]
				then mv $file "$TARGETDIR/$NEWNAME"
					echo "$SYSDATE File $file has moved correctly" >> $LOGFILENAME
				else echo "$SYSDATE File $file not contain UUID. Please, check file format" >> $LOGFILENAME
			fi
	done
}


check_lock() {
	flock -n 0
	if [[ $? -eq 0 ]]
	then
		move_func
		echo "Started script"
	else
		echo "Script already running!" >> $LOGFILENAME
		exit 1
	fi

}
check_lock


