import gradio as gr
import requests

def predict(year, adult_mortality, alcohol, hepatitis_b, measles, bmi,
            under_five_deaths, polio, total_expenditures, diphtheria,
            hiv_aids, gdp, schooling, thinness, country):
    
    payload = {
        "year": year,
        "adult_mortality": adult_mortality,
        "alcohol": alcohol,
        "hepatitis_b": hepatitis_b,
        "measles": measles,
        "bmi": bmi,
        "under_five_deaths": under_five_deaths,
        "polio": polio,
        "total_expenditures": total_expenditures,
        "diphtheria": diphtheria,
        "hiv_aids": hiv_aids,
        "gdp": gdp,
        "schooling": schooling,
        "thinness": thinness,
        "country": country
    }
    response = requests.post("http://localhost:8000/predict", json=payload)
    return response.json()["life_expectancy"]

ui = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Year"),
        gr.Number(label="Adult Mortality"),
        gr.Number(label="Alcohol"),
        gr.Number(label="Hepatitis B"),
        gr.Number(label="Measles"),
        gr.Number(label="BMI"),
        gr.Number(label="Under Five Deaths"),
        gr.Number(label="Polio"),
        gr.Number(label="Total Expenditures"),
        gr.Number(label="Diphtheria"),
        gr.Number(label="HIV/AIDS"),
        gr.Number(label="GDP"),
        gr.Number(label="Schooling"),
        gr.Number(label="Thinness"),
        gr.Textbox(label="Country"),
        ],
    outputs=gr.Number(label="Predicted Life Expectancy"),
    title="Life Expectancy Predictor",
    description="Predict life expectancy based on various health and demographic factors.",
)

ui.launch()