% Me borra todo lo anterior
clc
clear 

% EJERCICIO 4
% Un objeto se coloca en una habitacion que esta a temperatura constante de 25◦C. 
% Se sabe que la constante de enfriamiento del objeto es 0.02. 
% Al comienzo la temperatura del objeto es de 55◦C. 
% Considerando la ley de enfriamiento de Newton dada por 
% y′ = k(ta −y) 
% donde y denota la temperatura del objeto, k su constante de enfriamiento 
% y ta la temperatura ambiente 
% a) Que temperatura tendra el objeto despues de 50 minutos? 
% b) Cuanto tarda en ponerse a temperatura de 46◦C? 
% c) Que pasa con la temperatura despues de varias horas?
% k = 0.02 --> constante de enfriamiento
% ta = 25 --> temperatura ambiente

intervalo = [0 100];
y0 = 55;
f = @(t,y) 0.02 * (25 - y);
[t,y] = ode45(f, intervalo, y0);

% ITEM a
y50 = interp1(t, y, 50);
fprintf('Despues de 50 minutos el objeto estara a %f grados Celsius\n', y50);

% ITEM b
t46 = interp1(y, t, 46);
fprintf('\nTardara %f minutos en llegar a los 46 grados Celsius\n', t46);

% ITEM c
fprintf('\nDespues de varias horas, la temperatura cae exponencialmente.\n');

% Grafico el resultado
figure(1)
plot(t,y)
grid("on")


