from concert import Concierto, Usuario, EntradaGrada, EntradaPista, EntradaVIP

c1 = Concierto("Audrey Hobert", "Colonia", 30.0, 100)
c2 = Concierto("Lorde", "Bolonia", 60.0, 2000)
c3 = Concierto("Shego", "Granada", 30.0, 70)
conciertos = [c1, c2, c3]

nerea = Usuario("Nerea", 25)
julian = Usuario("Julián", 25)
terry = Usuario("Terry", 20)
usuarios = [nerea, julian, terry]

nerea.comprar_entrada(c1, "vip")
nerea.comprar_entrada(c2, "pista")
julian.comprar_entrada(c1, "grada")
julian.comprar_entrada(c3, "pista")
terry.comprar_entrada(c2, "vip")
terry.comprar_entrada(c3, "grada")

nerea.valorar(c1, 9)
julian.valorar(c3, 7)
terry.valorar(c2, 10)

total_entradas = 0
total_grada = 0
total_pista = 0
total_vip = 0
recaudacion_total = 0.0

concierto_mas = None
max_vendidas = 0
concierto_menos = None
min_vendidas = 0

for concierto in conciertos:
    vendidas = 0
    recaudacion_total += concierto.calcular_recaudacion()
    for entrada in concierto.entradas_vendidas:
        vendidas += 1
        total_entradas += 1
        if type(entrada) == EntradaGrada:
            total_grada += 1
        elif type(entrada) == EntradaPista:
            total_pista += 1
        elif type(entrada) == EntradaVIP:
            total_vip += 1

    if concierto_mas == None or vendidas > max_vendidas:
        concierto_mas = concierto
        max_vendidas = vendidas
    if concierto_menos == None or vendidas < min_vendidas:
        concierto_menos = concierto
        min_vendidas = vendidas

if total_entradas > 0:
    precio_medio = recaudacion_total / total_entradas
else:
    precio_medio = 0.0

print("Entradas vendidas en total:", total_entradas)
print("Entradas de pista:", total_pista)
print("Entradas de grada:", total_grada)
print("Entradas VIP:", total_vip)
print("Recaudación total:", recaudacion_total, "€")
print("Precio medio de las entradas:", precio_medio, "€")
print(f"Concierto con más entradas: {concierto_mas} ({max_vendidas})")
print(f"Concierto con menos entradas: {concierto_menos} ({min_vendidas})")