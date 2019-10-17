# Encuentra p* donde n es par p* = n(p * q) + 1
require 'prime'
def esPrimo(pe)
	print('Probando si '+pe.to_s+' es primo ... ')
	i = 2
	primo = Prime.prime?(pe);
	puts(pe.to_s+' es primo => '+primo.to_s+' ');
	return primo;
end
def encontrarPconNpar(pe, q)
	n = 2;
	i = 1;
	p_asterisco = n * (pe * q) + 1;

	puts('Probando con n = '+n.to_s+' y p* = '+p_asterisco.to_s+' ');
	while esPrimo(p_asterisco) == false
		i = i + 1;
		n = 2 * i;
		p_asterisco = n * (pe * q) + 1;
		puts('------------------------------------------------')
		puts('Probando con n = '+n.to_s+' y p* = '+p_asterisco.to_s+' ');
	end
	puts('---------- Resultado ---------------')
	puts('p* = '+n.to_s+' ( '+pe.to_s+' * '+q.to_s+' ) + 1 = '+p_asterisco.to_s+' ');
end
puts('Sea p* = n(p * q) + 1, se encontrará p* dado p y q');
puts('------------ Inputs -----------------')
puts('Introduzca p:')
pe = gets().chomp().to_i();
puts('Introduzca q:')
q = gets().chomp().to_i();
puts('----------- Fin Inputs ---------------');
encontrarPconNpar(pe, q);