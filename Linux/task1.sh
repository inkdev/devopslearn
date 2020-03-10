#!/bin/bash

help_func () {
	echo "Use script with following options:
	-t | --template - input template file
	-r | --result - output file with values"
	return 1
}



if [[ -z $* ]]
then
	echo "No arguments found!"
	exit 1
fi


OPTS=`getopt -o t:r: --long template:,result: -n 'task1.sh' -- "$@"`
#echo $OPTS
eval set -- "$OPTS"

#TEMPLATE=false
#RESULT=false


while true ; do
	case "$1" in
		-t | --template ) template="$2"; shift 2;;
		-r | --result ) result="$2"; shift 2;;
		-- ) shift; break;;
		*  ) break; exit 2;;
	esac
done

func_create(){ 
if [[ -z "$template" ]] || [[ -z "$result" ]]
then
	echo "Not found -t or -r parameter"
	help_func
	exit 2
fi

if [[ ! -f "$template" ]] && [[ ! -f "$result" ]]
then
	echo "File not found or not readable"
	exit 2
fi


cat $template | while read -r line ; do
    while [[ "$line" =~ (\$\{\{[a-zA-Z_][a-zA-Z_0-9]*\}\}) ]] ; do
	LHS=${BASH_REMATCH[1]}
	RHS="$(eval echo "\"$LHS\"")"
	line=${line//$LHS/$RHS}
    done
    echo "$line" >> $result
done


#echo TEMPLATE=$template
#echo RESULT=$result
echo "Complete!"
}
func_create
