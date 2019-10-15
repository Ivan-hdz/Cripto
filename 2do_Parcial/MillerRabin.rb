def esCongruente?(a, b, m)
	cong = false;
	if a == b
		cong = true
	else
		cong = ( (a - b) % m ) == 0 || ( (b - a) % m ) == 0	
	end
	puts(a.to_s + ' congruente ' + b.to_s + ' mod ' + m.to_s + ' | ' + cong.to_s );
	return cong;
end
def miller_rabin(a, n, iter)
	if n == 2 then
		return true;
	elsif n % 2 == 0 then	 
		return false;
	end
	n_1 = n - 1;
	c = n - 1;
	k = 0;
	while c % 2 == 0
		c = c / 2;
		k = k + 1;
	end
	b = ( (a ** c) % n );
	puts('Sea a = ' + a.to_s);
	puts('Sea n = ' + n.to_s );
	puts('Sea n - 1 = ' + n_1.to_s );
	puts('Dado (2 ^ k) * c = n - 1')
	puts('Encontradon k y c ... ');
	puts('c = ' + c.to_s  );
	puts('k = ' + k.to_s );
	puts('Dado b = (a ^ c) mod n ');
	puts('b = ' + b.to_s + ' mod ' + n.to_s );
	if esCongruente?(b, 1, n)
		return true
	end
	puts('Iterando ' + iter.to_s + ' veces');
	esPrimo = false;
	(0... iter).each do |i|
		puts('Iteración ' + (i+1).to_s + ': ' );
		if esCongruente(b, -1, n)
			puts('No es primo en la iteración ' + (i + 1 ).to_i);
		else
			b = (b ** 2) % n;
			esPrimo = true;
			break;
		end
	end
	return esPrimo
end
puts('------------ Inputs -----------------')
puts('Introduzca n:');
n = gets.chomp().to_i();
puts('Introduzca a:');
a = gets.chomp().to_i();
puts('Introduzca número de iteraciones:');
iter = gets.chomp().to_i();
puts('----------- Fin Inputs ---------------');
puts( miller_rabin(a, n, iter) );