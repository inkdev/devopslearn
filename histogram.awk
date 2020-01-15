{ arr[int($0/10)]++ }
END {
        step = 10
        count = 0

        for (i in arr)
        {

                if (count == 100) {
                        printf "%d : \t%6d ",count,arr[i]
                }
                else {
                        nr = count+step-1
                        printf "%3d - %3d : %d ",count,nr,arr[i]
                }
                for (j = 0; j < arr[i]; j++)
                        printf "*"
                printf "\n"
                count += step
        }
}
