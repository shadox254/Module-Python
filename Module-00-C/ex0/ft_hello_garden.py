from os import system

system('touch ft_hello_garden.c')
system('echo "#include <stdio.h>" > test.c')
system('echo "int main(){" >> test.c')
system('echo "printf(\\"Hello garden!!!!\\");}" >> test.c')
system('cc test.c')
system('./a.out')
system('rm ft_hello_garden.c a.out')