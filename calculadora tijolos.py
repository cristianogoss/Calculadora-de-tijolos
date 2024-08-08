import PySimpleGUI as sg
sg.theme("Reddit")

def calcular_area(altura, largura, qtd_tijolos):
    return qtd_tijolos * (altura * largura)


layout = [

    [sg.Text("Medidas da Parede")],
    [sg.Text("Altura (m)", size=(15,1)), sg.InputText(key = "altura")],
    [sg.Text("Largura (m)", size=(15,1)), sg.InputText(key = "largura")],
    [sg.Text("Tijolos (m²)", size=(15,1)), sg.InputText(key = "qtd_tijolos")],
    [sg.Button("Calcular"), sg.Button("Cancelar")],
    [sg.Text('', size=(40, 1), key='resultado')]
    
]

window = sg.Window('Cálculo de Tijolos', layout)

while True:
    event, values = window.read()
    if event in(sg.WINDOW_CLOSED, "Cancelar"):
        break
    if event == "Calcular":
        try:
            altura = float(values["altura"])
            largura = float(values["largura"])
            qtd_tijolos = float(values["qtd_tijolos"])
            
            if altura > 0 and largura > 0 and qtd_tijolos > 0:
                calculadora = calcular_area(altura, largura, qtd_tijolos)
                window["resultado"].update(f"{calculadora} Tijolos" )
            else: 
                window["resultado"].update("Por favor, insira valores maiores que zero")

        except ValueError:
            window["resultado"].update("Por favor, insira valores válidos")

window.close()
