require 'prime'
def esPrimo(pe)
	print('Probando si '+pe.to_s+' es primo ... ')
	i = 2
	primo = Prime.prime?(pe);
	puts(pe.to_s+' es primo => '+primo.to_s+' ');
	return primo;
end
puts('Número a probar si es primo:')
pe = gets.chomp.to_i;
esPrimo(pe);