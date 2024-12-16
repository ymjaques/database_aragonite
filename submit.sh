for f in job_*_*.sh ; do
    #echo $f
    sbatch $f
done
