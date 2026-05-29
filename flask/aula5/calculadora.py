import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        if operacao == "sqrt":
            if num1 < 0:
                resultado = "Erro"
                etapas = f"Não existe raiz real de {num1}."
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"
                
        else:
            num2_valor = request.form.get("num2", "").strip()
            if not num2_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe o segundo número para esta operação.",
                    resultados="",
                )
            num2 = float(num2_valor)

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"

            elif operacao == "-":
                resultado = num1 - num2 
                etapas = f"{num1} - {num2} = {resultado}"

            elif operacao == "*":
                resultado = num1 * num2 
                etapas = f"{num1} * {num2} = {resultado}"

            elif operacao == "/":
                if num2 == 0:
                    return render_template(
                        "calculadora.html",
                        etapas="Não é possível dividir por zero.",
                        resultados="Erro"
                    )
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"
            
            elif operacao == "**":
                resultado = num1 ** num2
                etapas = f"{num1}^{num2} = {resultado}"

            elif operacao == "log":
                if num1 <= 0 or num2 <= 0 or num2 == 1:
                    return render_template(
                        "calculadora.html",
                        etapas="Logaritmo exige base e logaritmando positivos, e base diferente de 1.",
                        resultados="Erro"
                    )
                resultado = math.log(num1, num2)
                etapas = f"log base {num2} ({num1}) = {resultado}"
            
            else:
                return render_template(
                    "calculadora.html",
                    etapas="Operação inválida.",
                    resultados="Erro"
                )

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado
        )

    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Digite apenas números válidos.",
            resultados="Erro"
        )