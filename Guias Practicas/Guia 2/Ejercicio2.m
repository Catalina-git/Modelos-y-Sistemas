% Me borra todo lo anterior
clc
clear 
% DATOS DE MATLAB
% ode45 me recuelve ecuaciones diferenciales, y es mas preciso que ode23.
% ode45 me devuelve dos vectores
% para definir una funcion f = @(parametros) funcion

% EJERCICIO 2
% En ciertas circunstancias, el numero de individuos en determinadas
% poblaciones de bacterias se rige por la ley y' = 0.2 * y
% Si al comienzo del experimento hay 30000 bacterias
% a) Cuantas habra 10 horas mas tarde?
% b) En que instante habra 100000 bacterias?

intervalo = [0 12];
y0 = 30000;
f = @(t,y) 0.2 * y;
% defino mis variables y que valores van a tomar
[t,y] = ode45(f, intervalo, y0);
% interpolo 
y10 = interp1(t, y, 10); % me pedian cunatas bacterias habia a las 10 horas, entonces esto es como evaluar a la solucion (ode) en 10
fprintf('A las 10 horas habra %f bacterias\n', y10);

y100000 = interp1(y, t, 100000); % me pedian en que momento hay cien mil bacterias
fprintf('\nHabra 100000 bacterias a los %f segundos', y100000);

% Grafico el resultado
figure(1)
plot(t,y)
grid("on")





