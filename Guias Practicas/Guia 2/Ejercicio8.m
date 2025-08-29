% Me borra todo lo anterior
clc
clear 

% EJERCICIO 8
% Considere el siguiente sistema del resorte
% a) Escriba la ecuacion diferencial que describe el sistema.
% b) Resuelva la ecuacion para m = 5kg, c = 1000Ns/m, k = 750N/m con una
% condicion inicial y(0) = 1m y velocidad inicial y'(0) = 0.5m/s.
% c) Escriba la represenacion en espacio de estado.
% d) Escriba el polinomio caracteristico del modelo y la solucion general.
% e) Resuelva en Matlab para los valores dados. Cambie de a uno los valores de los parametros y observe los diferentes resultados. 

% Parametros del sistema
m = 5;
c = 1000;
k = 750;

% ITEM a
% Ecuacion diferencial que describe el sistema
f = @(t,x) [x(2);-(c/m) * x(2) - (k/m) * x(1)]; % --> El ; me genera una matriz, el x(2) es la primer columna de la matriz y es la derivada primera
% --> c = b en la funcion de las diapositivas

x0 = [1;0.5]; % el ; me genera una columna
% Intervalo de integracion
intervalo = [0 10]; % intervalo = tspan, que es el tiempo de simulacion
[t,x] = ode45(f, intervalo, x0);

figure(1)
plot(t, x(:,1), 'b', 'DisplayName', 'Desplazamiento')
hold on
plot(t, x(:,2), 'r--', 'DisplayName', 'Velocidad')
xlabel('Tiempo (s)')
ylabel('Respuesta')
title('Desplazamiento y velocidad del sistema')
legend
grid on

