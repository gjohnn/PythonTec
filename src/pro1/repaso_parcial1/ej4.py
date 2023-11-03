"""Una empresa quiere pagar a sus empleados por la asistencia de lunes a viernes y un adicional por las
horas trabajadas los domingos en tareas especiales.
✔ El empleado asistió todo el mes, además entre 3 y 5 horas los domingos, adiciona el 3 % del sueldo.
✔ Si asistió todo el mes y entre 6 y 10 horas los domingos, adiciona el 10 %.
✔ No asistió todo el mes y entre 3 y 10 horas los domingos, adiciona el 2 %. """

salary = 1000

attendance = 0

while attendance<1 or attendance>2:
    attendance = int(input("Asistió todo el mes? (1-SI | 2- NO) : "))

if attendance == 1:

elif attendance == 2:
    