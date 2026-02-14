from os import system

system('touch ft_count_harvest_iterative.c')
system('echo "#include <stdio.h>" > ft_count_harvest_iterative.c')
system('echo "int main(){" >> ft_count_harvest_iterative.c')

system('echo "printf(\\"Days until harvest: \\");" >> ft_count_harvest_iterative.c')
system('echo "int f; scanf(\\"%d\\", &f);" >> ft_count_harvest_iterative.c')
system('echo "for(int i = 1; i <= f; i++){" >> ft_count_harvest_iterative.c')
system('echo "printf(\\"Day %d\\\\\\n\\", i);}" >> ft_count_harvest_iterative.c')
system('echo "printf(\\"Harvest time!\\");}" >> ft_count_harvest_iterative.c')

system('cc ft_count_harvest_iterative.c')
system('./a.out')
system('rm ft_count_harvest_iterative.c a.out')