{ arr[int($0/10)]++ }
END {
        count = 0

        for (i in arr)
        {

                if (int(i) < 10) {
                        nr = i*10+9
                        printf ("%3d - %3d : %6.1f ",i*10,nr,arr[i]/199*100)
                }
                else {
                        printf ("%d : \t%10.1f ",i*10,arr[i]/199*100)

        }
                for (j = 0; j < arr[i]; ++j)
                        printf "*"
                printf "\n"
                #count += 10

        }
}
