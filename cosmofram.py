# COSMOFARM - Agricultura Espacial
# Global Solution FIAP 2026

# definição do problema:

# Em missões espaciais de longa duração, como viagens para 
# Marte e permanência em bases na Lua, o transporte constante
# de alimentos da Terra é caro, limitado e pouco eficiente.
# Para garantir a segurança alimentar dos astronautas,
# torna-se necessário o uso de estufas espaciais capazes de
# produzir alimentos de forma autônoma e sustentável.
# O projeto COSMOFARM foi desenvolvido para auxiliar no
# gerenciamento de uma estufa espacial, permitindo o controle
# de plantas, monitoramento de sensores, análise de alertas
# e cálculo de recursos necessários para missões espaciais.

# A solução contribui para a produção de alimentos em
# ambientes extraterrestres, apoiando futuras missões para
# a Lua, Marte e outras regiões do espaço.
##################################################################

# lista 1 - Plantas da estufa
# nome, dias para colher, agua por dia (mL), calorias por 100g

plantas = [
    ["Tomate",        60, 15, 18],
    ["Ervilha",       70, 10, 81],
    ["Alface",        30,  8, 15],
    ["Rabanete",      25,  6, 16],
    ["Espinafre",     40,  9, 23],
    ["Cenoura",       75, 11, 41],
    ["Pepino",        55, 14, 15],
    ["Feijão-vagem",  60, 12, 31],
    ["Rucula",        28,  7, 25],
    ["Batata-doce",   90, 13, 86],
    ["Pimentão",      80, 16, 31],
    ["Couve",         45, 10, 49],
    ["Brocólis",      65, 11, 34],
    ["Soja",         100, 18,173],
    ["Trigo-anão",    95, 20,340],
    ["Beterraba",     55,  9, 43],
    ["Morango",       50, 12, 32],
    ["Erva-cidreira", 35,  6, 44],
    ["Manjericão",    30,  5, 23],
    ["Quinoa",        90, 15,368],
]


# lista 2 - Sensores da estufa
# nome, leitura atual, minimo ideal, maximo ideal

sensores = [
    ["Temperatura",        22.4, 18.0, 26.0],
    ["Umidade do ar",      71.3, 60.0, 80.0],
    ["CO2",               850.0,400.0,1200.0],
    ["Luminosidade",     5500.0,2000.0,8000.0],
    ["pH do Solo",          6.5,  6.0,  7.0],
    ["Umidade do solo",    55.0, 40.0, 70.0],
    ["Reservatório",       68.0, 20.0,100.0],
    ["Pressão interna",   101.3, 70.0,105.0],
    ["Nitrogênio",        210.0,100.0,300.0],
    ["Fósforo",            65.0, 30.0,100.0],
    ["Potássio",          280.0,150.0,400.0],
    ["Oxigênio",           20.9, 19.0, 23.0],
    ["Radiação UV",         2.1,  0.0,  5.0],
    ["Temp. da raiz",      20.5, 18.0, 24.0],
    ["Condutividade",       2.4,  1.5,  3.5],
    ["Velocidade do ar",    0.3,  0.1,  0.5],
    ["Energia usada (W)",  320.0, 0.0,500.0],
    ["Temp. painel solar", 45.2, 10.0, 80.0],
    ["Nivel nutrientes",   78.0, 50.0,100.0],
    ["Vibração",            0.1,  0.0,  2.0],
]


# lista 3 - Alertas do sistema
# id, nivel, mensagem, resolvido

alertas = [
    [1, "CRITICO", "pH do solo abaixo de 5.5", True ],
    [2, "AVISO",   "Umidade do ar acima de 85%", True ],
    [3, "INFO",    "Irrigação concluida com sucesso", True ],
    [4, "CRITICO", "Reservatório abaixo de 15%", False],
    [5, "AVISO",   "Temperatura acima de 27c", True ],
    [6, "INFO",    "Tomate pronto para colheita", True ],
    [7, "AVISO",   "CO2 abaixo de 400 ppm", True ],
    [8, "CRITICO", "Falha no sensor de luminosidade", True ],
    [9, "INFO",    "Colheita de alface: 320g", True ],
    [10, "AVISO",   "Deficiência de nitrogênio", True ],
    [11, "INFO",    "Dia 30 - todas as plantas normais", True ],
    [12, "CRITICO", "Pressão interna abaixo de 70 kPa", False],
    [13, "AVISO",   "Consumo de energia acima de 480W", True ],
    [14, "INFO",    "Sementes de quinoa plantadas", True ],
    [15, "AVISO",   "Crescimento lento na cenoura", True ],
    [16, "INFO",    "Manutenção preventiva realizada", True ],
    [17, "CRITICO", "Contaminação fungica no slot 03", False],
    [18, "AVISO",   "Bateria de backup com 28%", True ],
    [19, "INFO",    "Nodulação de bacterias confirmada", True ],
    [20, "AVISO",   "Potássio acima de 420 ppm", True ],
]


# lista 4 - Missoes espaciais
# nome, destino, duracao em dias, tripulantes

missoes = [
    ["Artemis IV",      "Lua",           30,  4],
    ["Mars Alpha",      "Marte",        520,  6],
    ["Gateway Hab-1",   "Orbita Lunar", 180,  3],
    ["ISS-EXT 2026",    "ISS",          365,  7],
    ["Mars Beta",       "Marte",        600,  8],
    ["Luna Base Camp",  "Lua",           90,  4],
    ["Deep Space 1",    "Cinturao",    1200,  5],
    ["Titan Probe",     "Tita",        2400,  0],
    ["Mars Gamma",      "Marte",        750, 10],
    ["Orbital Farm-1",  "LEO",          730,  6],
    ["Lunar Agri-Lab",  "Lua",          120,  3],
    ["Phobos Station",  "Phobos",       900,  4],
    ["Venus Flyby",     "Venus",        200,  0],
    ["Europa Lander",   "Europa",      1800,  0],
    ["ISS-Research",    "ISS",          180,  5],
    ["Mars Delta",      "Marte",        800, 12],
    ["Gateway Hab-2",   "Orbita Lunar", 365,  4],
    ["Ceres Outpost",   "Ceres",       1500,  3],
    ["Solar Sail Test", "LEO",           60,  0],
    ["Mars Epsilon",    "Marte",        550,  6],
]

# funções
def calcular_agua_total(lista_plantas):
    total = 0
    for planta in lista_plantas:
        total += planta[2]
        return total

def ver_plantas(plantas):
    print("PLANTAS DA ESTUFA ")
    print(f"{'Nome':<16} {'Dias':<8} {'Agua(mL)':<10} {'Cal/100g'}")
    print("-" * 45)

    for p in plantas:
        print(f"{p[0]:<16} {p[1]:<8} {p[2]:<10} {p[3]}")
        
total_agua = calcular_agua_total(plantas)

    print("-" * 45)
    print(f"Total de plantas  : {len(plantas)}")
    print(f"Agua total por dia: {total_agua} mL")

def verificar_sensores(sensores):
    print("SENSORES DA ESTUFA ")
    print(f"{'Sensor':<22} {'Leitura':<10} {'Status'}")
    print("-" * 45)

    ok = 0
    problema = 0

    for s in sensores:
        if s[1] < s[2]:
            status = "ABAIXO DO IDEAL"
            problema += 1
        elif s[1] > s[3]:
            status = "ACIMA DO IDEAL"
            problema += 1
        else:
            status = "OK"
            ok += 1
        print(f"{s[0]:<22} {s[1]:<10} {status}")

    print("-" * 45)
    print(f"Sensores OK  : {ok}")
    print(f"Com problema : {problema}")
    print(f"Saúde da estufa : {(ok / len(sensores) * 100):.0f}%")

def ver_alertas():
    print("ALERTAS DO SISTEMA ")
    print("Filtrar: [1] Todos  [2] CRITICO  [3] AVISO  [4] INFO")

    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Entrada inválida. Mostrando todos.")
        opcao = 1

    if opcao == 2:
        filtro = "CRITICO"
    elif opcao == 3:
        filtro = "AVISO"
    elif opcao == 4:
        filtro = "INFO"
    else:
        filtro = None

    print(f"\n{'ID':<5} {'Nivel':<10} {'Mensagem':<38} {'Resolvido'}")
    print("-" * 60)

    for a in alertas:
        if filtro is None or a[1] == filtro:
            res = "Sim" if a[3] else "NAO"
            print(f"{a[0]:<5} {a[1]:<10} {a[2]:<38} {res}")

    pendentes = sum(1 for a in alertas if not a[3])
    print(f" Alertas pendentes: {pendentes}")

def calcular_missao():
    print("CALCULAR NECESSIDADE DA MISSÃO ")

    while True:
        try:
            tripulantes = int(input("Número de tripulantes: "))
            if tripulantes >= 1:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite apenas números inteiros.")

    while True:
        try:
            dias = int(input("Duração da missão (dias): "))
            if dias >= 1:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite apenas números inteiros.")

    calorias_por_dia = 2500
    agua_por_dia = 2000  # mL por pessoa

    total_cal  = calorias_por_dia * tripulantes * dias
    total_agua = agua_por_dia * tripulantes * dias

    print(f"Tripulantes : {tripulantes}")
    print(f"Duração : {dias} dias")
    print(f"Calorias necessárias : {total_cal} kcal")
    print(f"Água para beber : {total_agua} mL ({total_agua // 1000} litros)")

# missoes com a duracao parecida

    print(" Missões com duração próxima:")
    achou = False
    for m in missoes:
        if abs(m[2] - dias) <= 90:
            print(f"  {m[0]} -> {m[1]}, {m[2]} dias, {m[3]} tripulantes")
            achou = True
    if not achou:
        print(" Nenhuma missão cadastrada com duração similar.")

def sobre():
    print("SOBRE O COSMOFARM")
    print("Problema: garantir a produção de alimentos em missões espaciais.")
    print("A COSMOFARM gerencia uma estufa espacial automatizada.")
    print("Controla plantas, sensores e alertas em missões.")
    print("Garante alimentação fresca na Lua, Marte e ISS.")
    print("Desenvolvido na Global Solution FIAP 2026.")
    print("ODS: 2 (Fome Zero), 9 (Inovação), 13 (Clima).")


# menu principal

def menu():
    while True:
        print("COSMOFARM - Agricultura Espacial")
        print("Global Solution FIAP 2026")
        print("[1] Ver plantas da estufa")
        print("[2] Verificar sensores")
        print("[3] Ver alertas")
        print("[4] Calcular necessidade da missão")
        print("[5] Sobre o sistema")
        print("[0] Sair")
 
        try:
            opcao = int(input("Escolha um número: "))
        except ValueError:
            print("Digite apenas números.")
            continue
 
        match opcao:
            case 1: 
                print()
                ver_plantas()
            case 2: 
                print()
                verificar_sensores()
            case 3:
                print()
                ver_alertas()
            case 4: 
                print()
                calcular_missao()
            case 5:
                print()
                sobre()
            case 0:
                print("Encerrando COSMOFARM. Boa missão!")
                break
            case _:
                print("Opção inválida.")
 
 
menu()