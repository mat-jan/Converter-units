from flask import Flask , render_template , request

app = Flask(__name__)

# Data to convert

kg_lbs = (2.205)
m_ft = (3.2808399)
c_f = (33.8)

#Short work

bad_option = "Please select correct options."
celcius = "°C"
fahrenheit = "°F"

#List of units

units = [
    {"value":"select", "label": "Selcent an option"},
    {"value": "kg", "label": "Kilograms (kg)"},
    {"value": "lbs", "label": "Pounds (lbs)"},    
    {"value": "m", "label": "Metrers (m)"},
    {"value": "ft", "label": "Foots (ft)"},
    {"value": "°C", "label": "Celcjus (°C)"},
    {"value": "°F", "label": "Fahrenheit (°F)"},
]


@app.route("/" , methods=["GET","POST"] )

def index ():
    #None
    data = None
    wynik = None
    converted_value = None
    
    #Data from html
    data = request.form.get("data_to_convert")

    unit_from = request.form.get("unit_from")
    print(unit_from)
    unit_to = request.form.get("unit_to")
    
    #Program
    if request.method == "POST":        
        try:
            data = float(data)
            if not data:
                wynik = "Please enter the value to be converted."
            else:

                if unit_from == "kg":               
                    if unit_to == "kg":
                        converted_value = data
                    elif unit_to == "lbs":
                        converted_value = convert_kg_to_lbs(data)
                    else:
                        wynik = bad_option
                
                elif unit_from == "lbs":
                    if unit_to == "lbs":
                        converted_value = data
                    elif unit_to == "kg":    
                        converted_value = convert_lbs_to_kg(data)
                    else:
                        wynik = bad_option
                
                elif unit_from == "m":
                    if unit_to == "m":
                        converted_value = data
                    elif unit_to == "ft":
                        converted_value = convert_m_to_ft(data)
                    else:
                        wynik = bad_option
                
                elif unit_from == "ft":
                    if unit_to == "ft":
                        converted_value = data
                    elif unit_to == "m":
                        converted_value = convert_ft_to_m(data)
                    else:
                        wynik = bad_option
                
                elif unit_from == celcius:
                    if unit_to == celcius:
                        converted_value = data
                    elif unit_to == fahrenheit:    
                        converted_value = convert_c_to_f(data)
                    else:
                        wynik = bad_option
                
                elif unit_from == fahrenheit:
                    if unit_to == fahrenheit:
                        converted_value = data
                    elif unit_to == celcius:    
                        converted_value = convert_f_to_c(data)
                    else:
                        wynik = bad_option
                        
                if converted_value is not None:
                    wynik = f"Your answer is {converted_value:.2f} {unit_to}. "
                else:
                    wynik = "ERROR: Please select corect units."
                    
                    
        except ValueError:
            wynik = "ERROR: Please enter a valid number."
            
    return render_template("index.html", wynik=wynik, units = units )
    

#Functions coverting

def convert_kg_to_lbs(data):
    return(data * kg_lbs)

def convert_lbs_to_kg(data):
    return(data / kg_lbs)

def convert_m_to_ft(data):
    return(data*m_ft)

def convert_ft_to_m(data):
    return(data/m_ft)

def convert_c_to_f(data):
    return(data*c_f)

def convert_f_to_c(data):
    return(data/c_f)


#Run app

if __name__ == "__main__":
    app.run("127.0.0.1" , port = 8080, debug = True)
    