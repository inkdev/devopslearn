{ var=int($_/10)
	++arr[var] }
END {
        count = 0

        for (i in arr)
        {

                if (int(i) < 10) {
                        nr = i*10+9
                        printf "%3d - %3d : %d ",i*10,nr,arr[i]
                }
                else {
                        printf "%d : \t%6d ",i*10,arr[i]

        }
                j=0
		while (j<arr[i])
		{
		printf "*"
		++j
			}
			printf "\n"

        }
}
