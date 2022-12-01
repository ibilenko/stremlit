import pandas as pd
import streamlit as st
import math

def d_calc(q):
    drec = 1000 * math.sqrt(4 * (q / 3600) / (3.14 * 2.2))

    if drec < 50:
        drec = 50

    if drec <= 65 and drec > 50:
        drec = 65

    if drec <= 80 and drec > 65:
        drec = 80

    if drec <= 100 and drec > 80:
        drec = 100

    if drec <= 125 and drec > 100:
        drec = 125

    if drec <= 150 and drec > 125:
        drec = 150

    if drec <= 200 and drec > 150:
        drec = 200

    if drec <= 250 and drec > 200:
        drec = 250

    if drec <= 300 and drec > 250:
        drec = 300

    if drec > 300:
        drec = 300

    return drec

st.title('Подбор станций CNP')

station_type=st.selectbox('Тип насосной станции', ('Повышения давления', 'Дренчерная', 'Спринклерная'))
n=st.selectbox('Количество основных насосов', (2,3,4))
model_df=pd.DataFrame()

col1_1, empty_col = st.columns(2)
col4_1, col4_2 = st.columns(2)
col2_1, col2_2 = st.columns(2)
col3_1, col3_2 = st.columns(2)

with col1_1:
    st.header("Параметры станции")
    q = st.number_input('Общая подача, м3/ч', min_value=0)
    drec=d_calc(q)
    H = st.number_input('Напор, м', min_value=0)
    Hp = st.number_input('Подпор на входе, м', min_value=0)

with col4_1:
    st.header("Основные насосы")
    pump_type=st.selectbox('Тип насосов', ('NES', 'CDM', 'TD'), key=0)
    if pump_type == 'CDM':
        ser=[1,3,5,10,15,20,32,42,65,85,120,150,200]
        index = 'Unnamed: 5'
        index2 = 'Unnamed: 0'
        model_df=pd.read_excel('Calc.xlsm', sheet_name='CDM IE3')
    elif pump_type == 'NES':
        ser = ['50/32', '65/40', '65/50', '80/65', '100/80', '125/100', '200/150']
        index = 'Unnamed: 5'
        index2 = 'Unnamed: 0'
        model_df=pd.read_excel('Calc.xlsm', sheet_name='NES')
    elif pump_type == 'TD':
        ser = [32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300]
        index = 'Unnamed: 7'
        index2 = 'Unnamed: 2'
        model_df=pd.read_excel('Calc.xlsm', sheet_name='TD+ TD G')
    pump_series = st.selectbox('Серия', ser, key=1)
    model_df = model_df[model_df[index]==pump_series]
    model=model_df[index2].tolist()
    pump_model = st.selectbox('Модель', model)

with col4_2:
    st.header("Жокей-насос")
    pump_type_jokey=st.selectbox('Тип насосов', ('NES', 'CDM', 'TD'), key=2)
    if pump_type_jokey == 'CDM':
        ser_jokey = [1,3,5,10,15,20,32,42,65,85,120,150,200]
    elif pump_type_jokey == 'NES':
        ser_jokey = ['50/32', '65/40', '65/50', '80/65', '100/80', '125/100', '200/150']
    elif pump_type_jokey == 'TD':
        ser_jokey = [32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 350]
    pump_series_jokey = st.selectbox('Серия', ser_jokey, key=3)
    #pump_model_jokey = st.selectbox('Модель', model_jokey, key=4)

with col2_1:
    st.header("Параметры коллекторов")
    mat_col = st.selectbox('Материал коллектора', ('Нержавеющая сталь', 'Углеродистая сталь'))
    type_col = st.selectbox('Тип коллектора', ('Цельный', 'Разрывной'))
    dcol = st.selectbox('Диаметр коллектора', (50, 65, 80, 100, 125, 150, 200, 250, 300))
    v = round((4 * q / 3600) / (3.14 * (dcol / 1000) * (dcol / 1000)), 2)

with col2_2:
    st.header("Калькулятор скорости")
    st.write(f'Рекомендуемый диаметр коллектора: {drec}')
    st.write(f'Скорость течения в коллекторе, м/с: {v}')

with col3_1:
    st.header("Автоматика")
    type_contr = st.selectbox('Тип контроллера', ('PD ES'))
    ip=st.selectbox('Степень защиты', ('65', '20'))

with col3_2:
    st.header("Доп. опции")









