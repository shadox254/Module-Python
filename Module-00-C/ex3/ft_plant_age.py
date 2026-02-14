from os import system

system('touch ft_plant_age.c')
system('echo "#include <stdio.h>" > ft_plant_age.c')
system('echo "int main(){" >> ft_plant_age.c')
system('echo "printf(\\"Enter plant age in days: \\");" >> ft_plant_age.c')
system('echo "int f; scanf(\\"%d\\", &f);" >> ft_plant_age.c')
system('echo "if(f > 60){" >> ft_plant_age.c')
system('echo "printf(\\"Plant is ready to harvest\\"); return 0;}" >> ft_plant_age.c')
system('echo "else{" >> ft_plant_age.c')
system('echo "printf(\\"Plant needs more time to grow\\"); return 0;}}" >> ft_plant_age.c')
system('cc ft_plant_age.c')
system('./a.out')
system('rm ft_plant_age.c a.out')