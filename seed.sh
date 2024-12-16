rm -f rngs.txt
for s in $(seq 1 100);
        do echo $RANDOM > rngs.txt
done
