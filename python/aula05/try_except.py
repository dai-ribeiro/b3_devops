def divide_numeros(dividendo, divisor):
    return dividendo / divisor

try:
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    resultado = divide_numeros(num1, num2)

except:
    print('Um erro foi detectado!')

# except (ZeroDivisionError, TypeError) as exc:
#     print(f'Divisão por zero ou erro de tipagem. ERROR: {exc}')
#
# except Exception:
#     print('Um erro foi detectado!')

else:
    print(resultado)

finally:
    print('Programa finalizado!')

