{ arr[int($0/10)]++ }
END {
        step = 10
        count = 0

        for (i in arr)
        {

                if (count == 100) {
                        printf ("%d : \t%10.1f ",count,arr[i]/199*100)
                }
                else {
                        nr = count+step-1
                        printf ("%3d - %3d : %6.1f ",count,nr,arr[i]/199*100)
                }
                for (j = 0; j < arr[i]; ++j)
                        printf "*"
                printf "\n"
                count += step
        }
}
