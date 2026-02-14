from os import system

system('touch ft_harvest_total.c')
system('echo "#include <stdio.h>" > ft_harvest_total.c')
system('echo "int main(){" >> ft_harvest_total.c')
system('echo "int total = 0;" >> ft_harvest_total.c')
system('echo "for(int i = 1; i <= 3; i++){" >> ft_harvest_total.c')
system('echo "printf(\\"Day %d harvest: \\", i);" >> ft_harvest_total.c')
system('echo "int f; scanf(\\"%d\\", &f); total += f;}" >> ft_harvest_total.c')
system('echo "printf(\\"Total harvest: %d\\", total);}" >> ft_harvest_total.c')
system('cc ft_harvest_total.c')
system('./a.out')
system('rm ft_harvest_total.c a.out')