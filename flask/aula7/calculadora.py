import math
from flask import render_template, request
 
 
def calcular():
    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template(
            "calculadora.html",
            etapas="Informe um valor válido para o primeiro número.",
            resultados="",
        )
 
    operacao = request.form.get("operacao", "+")
 
    if operacao == "sqrt":
        if num1 < 0:
            etapas = f"Não existe raiz real de {num1}."
            resultados = "Erro: número negativo"
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
            resultados = resultado
        return render_template("calculadora.html", etapas=etapas, resultados=resultados)
 
    if operacao == "log":
        if num1 <= 0:
            etapas = f"Logaritmo indefinido para {num1} (deve ser > 0)."
            resultados = "Erro: número inválido"
        else:
            resultado = math.log(num1)         
            etapas = f"ln({num1}) = {resultado}"
            resultados = resultado
        return render_template("calculadora.html", etapas=etapas, resultados=resultados)
 
    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="",
        )
 
    try:
        num2 = float(num2_valor)
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Valor inválido para o segundo número.",
            resultados="",
        )
 
    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
        resultados = resultado
 
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
        resultados = resultado
 
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
        resultados = resultado
 
    elif operacao == "/":
        if num2 == 0:
            etapas = "Divisão por zero é indefinida."
            resultados = "Erro: divisão por zero"
        else:
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultado}"
            resultados = resultado
 
    elif operacao == "**":
        resultado = math.pow(num1, num2)
        etapas = f"{num1} ^ {num2} = {resultado}"
        resultados = resultado

    elif operacao == "bhaskara":
        try:
            num3 = float(request.form.get("num3", "").strip())
        except ValueError:
            return render_template(
                "calculadora.html",
                etapas="Bhaskara precisa de três coeficientes (a, b, c).",
                resultados="",
            )
 
        a, b, c = num1, num2, num3
        delta = b**2 - 4 * a * c
 
        if a == 0:
            etapas = "Coeficiente 'a' não pode ser zero na fórmula de Bhaskara."
            resultados = "Erro: a = 0"
        elif delta < 0:
            etapas = (
                f"Δ = {b}² − 4·{a}·{c} = {delta}\n"
                "Δ < 0 → não há raízes reais."
            )
            resultados = "Sem raízes reais"
        elif delta == 0:
            x = -b / (2 * a)
            etapas = (
                f"Δ = {b}² − 4·{a}·{c} = {delta}\n"
                f"x = −({b}) / (2·{a}) = {x}"
            )
            resultados = f"x = {x} (raiz dupla)"
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b + sqrt_delta) / (2 * a)
            x2 = (-b - sqrt_delta) / (2 * a)
            etapas = (
                f"Δ = {b}² − 4·{a}·{c} = {delta}\n"
                f"x₁ = (−({b}) + √{delta}) / (2·{a}) = {x1}\n"
                f"x₂ = (−({b}) − √{delta}) / (2·{a}) = {x2}"
            )
            resultados = f"x₁ = {x1}  |  x₂ = {x2}"

    else:
        etapas = f"Operação '{operacao}' não reconhecida."
        resultados = "Erro: operação inválida"
 
    return render_template("calculadora.html", etapas=etapas, resultados=resultados)