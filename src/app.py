import streamlit as st

with st.sidebar:
    st.title('Calculadora IMC')
    st.header('Definição ')
    st.write('Índice de Massa Corporal (IMC)')
    st.write('É um índice que relaciona peso e altura de uma pessoa')
    st.write("Utilizado como medida de saúde geral, contudo, não considera o % de gordura corporal (BF)")
    
st.title("Calculadora")

peso = st.number_input(label='Seu peso em Quilograma (kg)', step=10.0, min_value=10.0)
altura = st.number_input(label='Sua altura em metros', min_value=1.0, step=0.10)

if st.button('Calcular'):
    imc = peso / (altura ** 2)
    imc_ideal = 22
    imc_delta = imc - imc_ideal
    
    if imc < 18.5:
        cf = 'Abaixo do peso'
    elif imc < 25:
        cf = 'Peso ideal'
    elif imc < 30:
        cf = 'Sobrepeso'
    elif imc < 40:
        cf = 'Obesidade'
    else:
        cf = 'Obesidade Grave'
    
    col1, col2 = st.columns(2)

    col1.metric(label="IMC Calculado", value=f"{imc:.2f}")
    col2.metric(label="Classificação", value=cf)
