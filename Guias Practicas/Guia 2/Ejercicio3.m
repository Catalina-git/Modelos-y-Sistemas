% Me borra todo lo anterior
clc
clear 

% EJERCICIO 3
% Se supone que la poblacion de un pais era de 39,5 millones en el año 2000
% y que crece siguiendo la ley de Maithus
% y' = 0.5 * y
% donde y(t) representa el numero de millones de habitantes en el instante
% t.
% a) Cuantos millones de habitantes habra en 2010?
% b) Cuando se alcanzaran los 50 millones de habitantes?

intervalo = [2000 2015];
y0 = 3.95e7;
f = @(t,y) 0.5 * y;
% defino mis variables y que valores van a tomar
[t,y] = ode45(f, intervalo, y0);

y2010 = floor(interp1(t, y, 2010));
fprintf('En el año 2010 habra %i habitantes\n', y2010);

t50 = ceil(interp1(y, t, 5e7));
fprintf('\nHabra 50 millones de habitantes en el año %i', t50);

% Grafico el resultado
figure(1)
plot(t,y)
grid("on")
