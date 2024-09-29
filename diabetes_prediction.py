import streamlit as st
import joblib

# 載入模型與標準化轉換模型
model = joblib.load('Diabetes_model.joblib')
scaler = joblib.load('Diabetes_scaler.joblib')

list1 = [0 for _ in range(33)]
st.title('糖尿病分類預測')
col1, col2, col3 = st.columns(3)

# Genetic Markers:
options0 = ('Negative', 'Positive')
# Autoantibodies：
options1 = ('Negative', 'Positive')
# Family History：
options2 = ('No', 'Yes')
# Environmental Factors：
options3 = ('Absent(不存在)', 'Present(存在)')
# Physical Activity：
options7 = ('Low', 'Moderate', 'High')
# Dietary Habits：
options8 = ('Healthy', 'Unhealthy')
# Ethnicity：
options13 = ('High Risk', 'Low Risk')
# Socioeconomic Factors：
options14 = ('Low', 'Medium', 'High')
# Smoking Status：
options15 = ('Non-Smoker', 'Smoker')
# Alcohol Consumption：
options16 = ('Low', 'Moderate', 'High')
# Glucose Tolerance Test：
options17 = ('Abnormal(異常)', 'Normal')
# History of PCOS：
options18 = ('No', 'Yes')
# Previous Gestational Diabetes：
options19 = ('No', 'Yes')
# Pregnancy History：
options20 = ('Complications', 'Normal')
# Cystic Fibrosis Diagnosis：
options24 = ('No', 'Yes')
# Steroid Use History：
options25 = ('No', 'Yes')
# Genetic Testing：
options26 = ('Negative', 'Positive')
# Liver Function Tests：
options28 = ('Abnormal(異常)', 'Normal')
# Urine Test：
options30 = ('Glucose Present(葡萄糖)', 'Ketones Present(酮體)', 'Normal', 'Protein Present(尿蛋白)')
# Early Onset Symptoms：
options32 = ('No', 'Yes')

columns = ['Genetic Markers(遺傳標記)',
           'Autoantibodies(自體抗體)',
           'Family History(家族病史)', 
           'Environmental Factors(環境因素)',
           'Insulin Levels(胰島素濃度)',
           'Age',
           'BMI',
           'Physical Activity(體能活動)',
           'Dietary Habits(飲食習慣)',
           'Blood Pressure(血壓)',
           'Cholesterol Levels(膽固醇含量)',
           'Waist Circumference(腰圍)',
           'Blood Glucose Levels(血糖值)',
           'Ethnicity(族群)',
           'Socioeconomic Factors(社會經濟因素)',
           'Smoking Status(吸煙狀況)',
           'Alcohol Consumption(飲酒)',
           'Glucose Tolerance Test(葡萄糖耐量試驗)',
           'History of PCOS(多囊性卵巢綜合症)', 
           'Previous Gestational Diabetes(妊娠性糖尿病病史)',
           'Pregnancy History(懷孕病史)',
           'Weight Gain During Pregnancy(孕期體重增加)',
           'Pancreatic Health(胰臟健康)',
           'Pulmonary Function(肺功能)',
           'Cystic Fibrosis Diagnosis(囊腫性纖維化診斷)',
           'Steroid Use History(類固醇使用史)',
           'Genetic Testing(基因檢測)',
           'Neurological Assessments(神經學檢查)',
           'Liver Function Tests(肝功能測試 )',
           'Digestive Enzyme Levels(消化酶水平)',
           'Urine Test(尿液檢查)',
           'Birth Weight(出生體重)',
           'Early Onset Symptoms(早發性癥狀)']

with col1:
    list1[0] = options0.index(st.radio(f'{columns[0]}:', options0))
    list1[1] = options1.index(st.radio(f'{columns[1]}:', options1))
    list1[2] = options2.index(st.radio(f'{columns[2]}:', options2))
    list1[3] = options3.index(st.radio(f'{columns[3]}:', options3))
    list1[4] = st.slider(f'{columns[4]}:', value=21, min_value=5, max_value=50, step=1)
    st.write('Values:', list1[4])
    list1[5] = st.slider(f'{columns[5]}:', value=30, min_value=0, max_value=80, step=1)
    st.write('Values:', list1[5], "years old")
    list1[6] = st.slider(f'{columns[6]}:', value=25.0, min_value=12.0, max_value=40.0, step=0.1)
    st.write('Values:', list1[6])
    list1[7] = options7.index(st.radio(f'{columns[7]}:', options7))
    list1[8] = options8.index(st.radio(f'{columns[8]}:', options8))
    list1[9] = st.slider(f'{columns[9]}:', value=110.5, min_value=60.0, max_value=150.0, step=0.1)
    st.write('Values:', list1[9], 'mmHg')
    list1[10] = st.slider(f'{columns[10]}:', value=190.0, min_value=100.0, max_value=300.0, step=1.0)
    st.write('Values:', list1[10])
with col2:
    list1[11] = st.slider(f'{columns[11]}:', value=35.0, min_value=20.0, max_value=55.0, step=0.1)
    st.write('Values:', list1[11], 'inches')
    list1[12] = st.slider(f'{columns[12]}:', value=160.0, min_value=80.0, max_value=300.0, step=1.0)
    st.write('Values:', list1[12], 'mg/dL')
    list1[13] = options13.index(st.radio(f'{columns[13]}:', options13))
    list1[14] = options14.index(st.radio(f'{columns[14]}:', options14))
    list1[15] = options15.index(st.radio(f'{columns[15]}:', options15))
    list1[16] = options16.index(st.radio(f'{columns[16]}:', options16))
    list1[17] = options17.index(st.radio(f'{columns[17]}:', options17))
    list1[18] = options18.index(st.radio(f'{columns[18]}:', options18))
    list1[19] = options19.index(st.radio(f'{columns[19]}:', options19))
    list1[20] = options20.index(st.radio(f'{columns[20]}:', options20))
    list1[21] = st.slider(f'{columns[21]}:', value=15.0, min_value=0.0, max_value=40.0, step=0.1)
    st.write('Values:', list1[21], 'Kg')
    
with col3:
    list1[22] = st.slider(f'{columns[22]}:', value=47.0, min_value=10.0, max_value=100.0, step=1.0)
    st.write('Values:', list1[22])
    list1[23] = st.slider(f'{columns[23]}:', value=70.0, min_value=30.0, max_value=90.0, step=1.0)
    st.write('Values:', list1[23])
    list1[24] = options24.index(st.radio(f'{columns[24]}:', options24))
    list1[25] = options25.index(st.radio(f'{columns[25]}:', options25))
    list1[26] = options26.index(st.radio(f'{columns[26]}:', options26))
    list1[27] = st.slider(f'{columns[27]}:', value=1.8, min_value=1.0, max_value=3.0, step=0.01)
    st.write('Values:', list1[27])
    list1[28] = options28.index(st.radio(f'{columns[28]}:', options28))
    list1[29] = st.slider(f'{columns[29]}:', value=46.0, min_value=10.0, max_value=100.0, step=1.0)
    st.write('Values:', list1[29])
    list1[30] = options30.index(st.radio(f'{columns[30]}:', options30))
    list1[31] = st.slider(f'{columns[31]}:', value=3097.0, min_value=1500.0, max_value=4500.0, step=0.1)
    st.write('Values:', list1[31], 'g')
    list1[32] = options32.index(st.radio(f'{columns[32]}:', options32))

labels = ['Cystic Fibrosis-Related Diabetes (CFRD,囊腫性纖維化相關糖尿病)', 'Gestational Diabetes(妊娠糖尿病)', 'LADA(1.5型糖尿病,潛伏性成人自體免疫糖尿病)', 'MODY(年輕早發型糖尿病)', 'Neonatal Diabetes Mellitus (NDM,新生兒糖尿病)', 'Prediabetic(糖尿病前期)', 'Secondary Diabetes(繼發性糖尿病)', 'Steroid-Induced Diabetes(類固醇誘發糖尿病)', 'Type 1 Diabetes(第1型糖尿病)', 'Type 2 Diabetes(第2型糖尿病)', 'Type 3c Diabetes(3C型糖尿病) (Pancreatogenic Diabetes,胰腺源性糖尿病)', 'Wolcott-Rallison Syndrome(Wolcott-Rallison綜合徵)', 'Wolfram Syndrome(Wolfram綜合徵)']
if st.button('預測'):
    X_new = [list1]
    X_new = scaler.transform(X_new)
    st.write(f'### 預測糖尿病類型：{labels[model.predict(X_new)[0]]}')
