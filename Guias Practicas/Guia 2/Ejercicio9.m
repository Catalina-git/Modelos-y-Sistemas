% Me borra todo lo anterior
clc
clear 

% EJERCICIO 9
% Los balances de masa se utilizan en ingenieria para realizar modelos compartimentales. 
% En esencia establecen que la variacion de la masa en un compartimento 
% es igual al flujo de masa entrante menos el de la saliente por unidad de tiempo; 
% i.e. m' = me' - ms' donde m denota la masa total por unidad de tiempo, 
% me la masa entrante y ms la masa saliente.
% Usando un balance de masa, determina un sistema de ecuaciones que modelice 
% la altura de los depositos en la Figura en cada instante de tiempo 
% suponiendo que:
% (a) el liquido que fluye es agua
% (b) el area de los depositos es a1,a2 > 0, respectivamente 
% (c) inicialmente los depositos estan vacios y a partir de ese instante 
% el agua fluye continuamente
% (d) el flujo de agua entre los depositos es proporcional a la diferencia 
% x1(t)−x2(t) con una constante 1/R1
% (e) el flujo de salida del segundo deposito es proporcional a x2(t) 
% con una constante 1/R2
% (f) el caudal de entrada es tal que los depositos nunca se llenan 
% ni vacian completamente.


% Parámetros del sistema
a1 = 1;           % Área del depósito 1
a2 = 1;           % Área del depósito 2
R1 = 2;           % Resistencia entre depósitos
R2 = 3;           % Resistencia de salida
caudal_in = 1;    % Caudal de entrada constante

% Sistema de ecuaciones diferenciales
f = @(t, x) [(1/a1)*(caudal_in - (1/R1)*(x(1) - x(2)));        % dx1/dt
    (1/a2)*((1/R1)*(x(1) - x(2)) - (1/R2)*x(2))];              % dx2/dt

% Condiciones iniciales
x0 = [0; 0];  % Ambos depósitos vacíos

% Simulación
intervalo = [0 50];
[t, x] = ode45(f, intervalo, x0);

% Gráfico
figure(1)
plot(t, x(:,1), 'b', 'LineWidth', 2, 'DisplayName', 'Depósito 1')
hold on
plot(t, x(:,2), 'r', 'LineWidth', 2, 'DisplayName', 'Depósito 2')
xlabel('Tiempo [s]')
ylabel('Altura del agua')
legend
title('Evolución de las alturas del agua en los depósitos')
grid on

