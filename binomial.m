clc;clear; close all; 

% Distribucion Binomial
N=128;
P=0.5;
x = 0:N;

% Grafico de la funcion de probabilidad
y=binopdf(x,N,P);
plot(x,y,'-o','LineWidth',2)
% Caracteristicas del grafico
grid on; grid minor
ax=gca;
ax.XLim=[0 128]; ax.XTick=ax.XLim(1):4:ax.XLim(2);
ax.YLim=[0 0.075]; ax.YTick=ax.YLim(1):0.005:ax.YLim(2);
ylabel('Probabilidad')
xlabel('Numero de bits distintos')
title('Distancias de Hamming: funcion de probabilidad.')

% Grafico de funcion de distribucion de probabilidad
% Distribucion
figure
y=cdf('Binomial',x,128,0.5);
plot(x,y,'LineWidth',2)
% Caracteristicas del grafico
grid on; grid minor
ax=gca;
ax.XLim=[0 128]; ax.XTick=ax.XLim(1):10:ax.XLim(2);
ax.YLim=[0 1]; ax.YTick=ax.YLim(1):0.125:ax.YLim(2);
ylabel('Probabilidad acumulada')
xlabel('Numero de bits distintos')
title('Distancias de Hamming: funcion de distribucion de probabilidad.')
