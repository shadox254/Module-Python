from os import system

system('touch ft_count_harvest_recursive.c')
system('echo "#include <stdio.h>" > ft_count_harvest_recursive.c')

system('echo "void ft_count_harvest_recursive(int day, int count){" >> ft_count_harvest_recursive.c')
system('echo "if(count <= day){" >> ft_count_harvest_recursive.c')
system('echo "printf(\\"Day %d\\\\\\n\\", count); count++;" >> ft_count_harvest_recursive.c')
system('echo "ft_count_harvest_recursive(day, count);}" >> ft_count_harvest_recursive.c')
system('echo "}" >> ft_count_harvest_recursive.c')


system('echo "int main(){" >> ft_count_harvest_recursive.c')
system('echo "printf(\\"Days until harvest:\\");" >> ft_count_harvest_recursive.c')
system('echo "int f; scanf(\\"%d\\", &f);" >> ft_count_harvest_recursive.c')
system('echo "ft_count_harvest_recursive(f, 1);" >> ft_count_harvest_recursive.c')
system('echo "printf(\\"Harvest time!\\");}" >> ft_count_harvest_recursive.c')

system('cc ft_count_harvest_recursive.c')
system('./a.out')
system('rm ft_count_harvest_recursive.c a.out')