#!/bin/bash
#SBATCH --job-name=arg%(jstart)s_%(jstop)s
#SBATCH --account=johnt447
#SBATCH -o job_%(jstart)s_%(jstop)s.out
#SBATCH -e job_%(jstart)s_%(jstop)s.err
#SBATCH --time=3-00:00:00
###SBATCH --time=15:00
#SBATCH --mem-per-cpu=1G
###SBATCH --partition=test
#SBATCH --partition=small
###SBATCH --ntasks=100
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40

module purge
module load gcc/9.3.0 openmpi/4.0.3 fftw/3.3.8-mpi

PATH=/projappl/johnt447/lammps/lammps-3Mar20/src:$PATH ; export PATH
PATH=/users/moraisja/bin:$PATH ; export PATH

#srun lmp_intel2 -in defect.lmp
#srun lmp_mahti -sf omp -in in.lmp

parallel -j 1 --resume --joblog jobs_%(jstart)s_%(jstop)s.log "cd arg_{}; srun lmp_mahti -in defect.lmp; srun lmp_mahti -sf omp -in in.lmp" ::: {%(jstart)s..%(jstop)s}

