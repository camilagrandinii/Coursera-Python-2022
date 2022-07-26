segundos_str = input()
total_segs = int(segundos_str)

horas = total_segs // 3600
dias = horas // 24
horas = horas % 24
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60
print(horas)

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")