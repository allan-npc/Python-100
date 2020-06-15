from math import cos, sin, tan, radians
an = float(input('Digite o ângulo: '))
rad = radians(an)
print(f'O seno do ângulo {an} é {round(sin(an),2)} rad, o cosseno {round(cos(an),2)} rad e a tangente {round(tan(an),2)} rad \n Em graus os valores são: {round(sin(rad),2)}°, {round(cos(rad),2)}° e {round(tan(rad),2)}°')