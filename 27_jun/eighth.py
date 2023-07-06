input_seconds = int(input('Ingresa los segundos que quieres convertir: '))

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR

minutes_by_seconds = input_seconds / SECONDS_IN_MINUTE
hours_by_seconds = input_seconds / SECONDS_IN_HOUR

print(f"{input_seconds} son {minutes_by_seconds} minutos")
print(f"{input_seconds} son {hours_by_seconds} horas")