from os import system

system('touch ft_plot_area.c')
system('echo "#include <stdio.h>" > ft_plot_area.c')
system('echo "int main(){" >> ft_plot_area.c')
system('echo "printf(\\"Enter length: \\");" >> ft_plot_area.c')
system('echo "int f; scanf(\\"%d\\", &f);" >> ft_plot_area.c')
system('echo "printf(\\"Enter width: \\");" >> ft_plot_area.c')
system('echo "printf(\\"Enter width: \\");" >> ft_plot_area.c')
system('echo "int g; scanf(\\"%d\\", &g);" >> ft_plot_area.c')
system('echo "int res = f*g; printf(\\"Plot area: %d\\", res);}" >> ft_plot_area.c')
system('cc ft_plot_area.c')
system('./a.out')
system('rm ft_plot_area.c a.out')