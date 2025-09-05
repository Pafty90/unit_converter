from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'converter/index.html')

def weight(request):
    return render(request, 'converter/weight.html')

def temperature(request):
    return render(request, 'converter/temperature.html')

def result(request):
    if request.method == "POST":
        if request.POST.get("from_unit") == request.POST.get("to_unit"):
            value = float(request.POST.get("length") or request.POST.get("weight") or request.POST.get("temperature"))
            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")
            result_value = value
        else:
            result_value = None
            if request.POST.get("length"):
                value = float(request.POST.get("length"))
                from_unit = request.POST.get("from_unit")
                to_unit = request.POST.get("to_unit")
                LENGTH_UNITS = {
                    "mm": 0.001,   # 1 mm = 0.001 m
                    "cm": 0.01,    # 1 cm = 0.01 m
                    "m": 1,        # base = meter
                    "km": 1000,
                    "in": 0.0254,
                    "ft": 0.3048,
                    "yd": 0.9144,
                    "mi": 1609.34,
                }
                result_value = value * LENGTH_UNITS[from_unit] / LENGTH_UNITS[to_unit]
            elif request.POST.get("weight"):
                value = float(request.POST.get("weight"))
                from_unit = request.POST.get("from_unit")
                to_unit = request.POST.get("to_unit")
                WEIGHT_UNITS = {
                    "mg": 0.001,   # 1 mg = 0.001 g
                    "g": 1,        # base = gram
                    "kg": 1000,
                    "oz": 28.3495,
                    "lb": 453.592,
                }
                result_value = value * WEIGHT_UNITS[from_unit] / WEIGHT_UNITS[to_unit]
            elif request.POST.get("temperature"):
                value = float(request.POST.get("temperature"))
                from_unit = request.POST.get("from_unit")
                to_unit = request.POST.get("to_unit")
                # Convert to Celsius first
                if from_unit == "c":
                    celsius = value
                elif from_unit == "f":
                    celsius = (value - 32) * 5/9
                elif from_unit == "k":
                    celsius = value - 273.15

                # Convert Celsius to target
                if to_unit == "c":
                    result_value = celsius
                elif to_unit == "f":
                    result_value = (celsius * 9/5) + 32
                elif to_unit == "k":
                    result_value = celsius + 273.15

        context = {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": str(round(result_value, 2)),
        }
        if request.POST.get("length"):
            context["length"] = request.POST.get("length")
        elif request.POST.get("weight") :
            context["weight"] = request.POST.get("weight")
        elif request.POST.get("temperature"):
            context["temperature"] = request.POST.get("temperature")

        return render(request, "converter/result.html", context)
    else:
        return render(request, "converter/result.html")