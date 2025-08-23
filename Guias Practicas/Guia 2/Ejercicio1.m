% Me borra todo lo anterior
clc
clear 

% EJERCICIO 1
% Hallar la solucion del problema de valor inicial 
% y′ = y − 1 
% y(0) = 2 
% en el intervalo [0,7].

intervalo = [0 7];
y0 = 2;
f = @(t,y) y - 1;
% defino mis variables y que valores van a tomar
[t,y] = ode45(f, intervalo, y0);

% Grafico el resultado
figure(1)
plot(t,y)
grid("on")
