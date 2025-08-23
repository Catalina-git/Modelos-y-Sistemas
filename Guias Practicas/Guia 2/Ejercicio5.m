% Me borra todo lo anterior
clc
clear 

% EJERCICIO 5
% Dibujar en la misma ventana grafica las soluciones correpondientes a la
% ley lineal 
% y' = -y + t 
% en el intervalo [0, 20] considerando distintos valores de y(0) entre -10
% y 10. Analizar los resultados.

intervalo = [0 20];
y0_valores = -10:1:10; % planteo un array que va de -10 a 10, con un paso de 1
f = @(t,y) -y + t;

for y0 = y0_valores
    [t,y] = ode45(f, intervalo, y0);
    % Grafico el resultado
    figure(1)
    hold on % Mantiene el grafico actual y me deja ir agregando nuevos elementos sin borrar lo que ya esta dibujado
    grid("on")
    plot(t,y)
end



