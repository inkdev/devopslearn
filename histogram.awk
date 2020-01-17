{ arr[int($0/10)]++ }
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
                for (j = 0; j < arr[i]; ++j)
                        printf "*"
                printf "\n"
                #count += 10

        }
}
