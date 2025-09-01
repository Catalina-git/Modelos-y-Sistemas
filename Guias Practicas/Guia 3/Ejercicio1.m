% Me borra todo lo anterior
clc
clear

% EJERCICIO 1
% ----------------------------------- ITEM d -----------------------------------
% Graficar las variables de estado en funciondel tiempo para el sistema
% autonomo (sistema autonomo --> u(t) = 0)

% Vector de tiempo
t = linspace(0,5,500);

% Sistema autonomo
x1_h = 3 * exp(-t) - 2 * exp(-2 * t); % La h es porque es un sistema autonomo --> homogeneo
x2_h = -3 * exp(-t) - 4 * exp(-2 * t);

% Grafico de la solucion del sistema autonomo 
figure(1);
plot(t, x1_h, 'g', 'LineWidth', 2, 'DisplayName', 'x1(t)');
hold on;
plot(t, x2_h, 'r', 'LineWidth', 2, 'DisplayName', 'x2(t)');
xlabel('t [s]');
ylabel('Variables');
title('Variables de estado del sistema autónomo');
legend;
grid on;

% ----------------------------------- ITEM e -----------------------------------
% raficar las variables de estado para el sistema no-homogeneo siendo la
% entrada u(t) = 1, para todo t >= 0 y B = (0:1) (B es una matriz de una
% columna por una fila).

% Uso el mismo vector del tiempo que para el sistema homogeneo

% Solucion del sistema no-homogeneo --> xh(t) + xp(t)
% --> solucion homogenea + solucion particular
% La solucion particular es la integral de 0 a t, de phi(t-tau)*B*u(tau) dtau
% Esa integral la resolvi a mano
x1_p = -exp(-t) + 0.5 * exp(-2*t) + 0.5;
x2_p = exp(-t) - exp(-2*t);

%Entonces la solucion del sistema no-homogeneo es...
x1_nh = x1_h + x1_p;
x2_nh = x2_h + x2_p;

% Grafico de la solucion del sistema no-homogeneo 
figure(2);
plot(t, x1_nh, 'g', 'LineWidth', 2, 'DisplayName', 'x1(t)');
hold on;
plot(t, x2_nh, 'r', 'LineWidth', 2, 'DisplayName', 'x2(t)');
xlabel('t [s]');
ylabel('Variables');
title('Variables de estado del sistema no-homogéneo');
legend;
grid on;