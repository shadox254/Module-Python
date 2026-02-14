from os import system

system('touch ft_garden_summary.c')
system('echo "#include <stdio.h>" > ft_garden_summary.c')
system('echo "int main(){" >> ft_garden_summary.c')
system('echo "printf(\\"Enter garden name: \\");" >> ft_garden_summary.c')
system('echo "char *f; scanf(\\"%s\\", f);" >> ft_garden_summary.c')
system('echo "printf(\\"Enter number of plants: \\");" >> ft_garden_summary.c')
system('echo "int g; scanf(\\"%d\\", &g);" >> ft_garden_summary.c')

system('echo "printf(\\"Garden: %s\\\\\\n\\", f);" >> ft_garden_summary.c')
system('echo "printf(\\"Plants: %d\\\\\\n\\", g);" >> ft_garden_summary.c')
system('echo "if(g > 0){" >> ft_garden_summary.c')
system('echo "printf(\\"Status: Growing well!\\");}}" >> ft_garden_summary.c')

system('cc ft_garden_summary.c')
system('./a.out')
system('rm ft_garden_summary.c a.out')