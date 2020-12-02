def convertCurrency(value, orig, new):
    import requests, json
    url = f"https://api.ratesapi.io/api/latest?base={orig}&symbols={new}"
    try:
        value = float(value)
        r = requests.get(url)
        stringContent = r.content.decode("utf8")

        jsonData = json.loads(stringContent)

        rate = jsonData.get("rates").get(new)

        exchangeValue = rate * value

        return str(exchangeValue)
    except:
        return "NaN"

def getCurrencyCodes():
    f = open("currencyCodes.txt", "r+")
    toReturn = []

    for cc in f.readlines():
        toReturn.append(cc.strip())

    
    
    return sorted(toReturn)


def menu():
    import PySimpleGUI as sg
    import json

    layout = [
        [sg.Text("Currency Converter")],
        [sg.InputText(key="ov")],
        [sg.Text("Original Currency"), sg.Combo(getCurrencyCodes(), key="oc", size=(4, 400))],
        [sg.Text("New Currency"), sg.Combo(getCurrencyCodes(), key="nc", size=(4, 400))],
        [sg.Button("convert")],
        [sg.Text(" " * 20, key="nv")]
        ]

    window = sg.Window("Currency Converter", layout, element_justification = 'c')

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "convert":
            print(value.keys())
            toConvert = value["ov"]
            toConvertFrom = value["oc"]
            toConvertTo = value["nc"]
            converted = convertCurrency(toConvert, toConvertFrom, toConvertTo)
            window.Element("nv").Update(converted)
            
    window.close()

    
    


menu()
