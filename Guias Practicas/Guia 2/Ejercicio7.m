% Me borra todo lo anterior
clc
clear 

% EJERCICIO 7
% En algunos modelos de pesca se utiliza la ecuacion 
% y′ = α * y * ln(k/y) − qy 
% donde el termino −qy mide el efecto negativo que ejerce la pesca sobre 
% el crecimiento de la poblacion. 
% Estos modelos ayudan a analizar la sostenibilidad de los bancos de pesca. 
% Calcular y dibujar en un mismo grafico las soluciones del problema 
% para α = 0.2, k = 27 e y(0) = 10, 
% variando los valores del parametro q : 0,0.05,0.1,0.2,0.3.

alpha = 0.2;
k = 27;
y0 = 10;
intervalo = [0 50];

q_valores = 0:0.05:0.3; % planteo un array que va de 0 a 0.3, con un paso de 0.05

figure(1)
hold on % Mantiene el grafico actual y me deja ir agregando nuevos elementos sin borrar lo que ya esta dibujado


for i = 1:length(q_valores)
    q = q_valores(i);

    % Defino la funcion
    f = @(t,y) alpha * y * log(k/y) - q * y;
    % Resuelvo con ode
    [t,y] = ode45(f, intervalo, q);

    % Grafico el resultado
    plot(t, y, 'LineWidth', 2, 'DisplayName', ['q = ' num2str(q)]) % Asi pongo que linea corresponde a que valor de q
end

% Etiquetas y leyenda
xlabel('Tiempo')
ylabel('Poblacion de peces y(t)')
title('Modelo de pesca con distintos valores de q')
legend 
grid on