import os
import csv
import random

def generate_blood_pressure(status):
    if status == 'normal':
        systolic = random.randint(110, 129)
        diastolic = random.randint(70, 84)
    elif status == 'high':
        systolic = random.randint(130, 180)
        diastolic = random.randint(85, 110)
    else:
        systolic = random.randint(110, 160)
        diastolic = random.randint(70, 100)
    return f"{systolic}/{diastolic}"

def get_disease_info(folder_name):
    if 'abnormal_heartbeat' in folder_name.lower():
        return {
            'Doença': 'Arritmia Cardíaca',
            'Descrição': 'Ritmo cardíaco irregular, podendo bater muito rápido ou muito devagar.',
            'Sintomas': 'Palpitações, falta de ar, tontura, desconforto no peito.',
            'Tratamento': 'Betabloqueadores, antiarrítmicos, ablação por cateter, marca-passo.',
            'Idade': random.randint(30, 85),
            'Nivel de glicemia': f"{random.randint(75, 120)} mg/dL",
            'Pressão arterial': generate_blood_pressure('irregular'),
            'Nivel de colesterol': f"{random.randint(150, 240)} mg/dL",
            'Oxigenação': f"{random.randint(94, 98)} %",
            'Nivel de creatinina': f"{round(random.uniform(0.7, 1.4), 1)} mg/dL"
        }
    elif 'myocardial_infarction' in folder_name.lower():
        age = random.randint(45, 90)
        return {
            'Doença': 'Infarto do Miocárdio',
            'Descrição': 'Ataque cardíaco agudo, morte de parte do tecido muscular do coração devido a isquemia.',
            'Sintomas': 'Dor severa no peito (irradiando para braço esquerdo/mandíbula), sudorese fria, náusea, falta de ar extrema.',
            'Tratamento': 'Angioplastia coronariana, trombolíticos, aspirina, betabloqueadores e estatinas, reabilitação cardíaca urgente.',
            'Idade': age,
            'Nivel de glicemia': f"{random.randint(90, 180)} mg/dL",
            'Pressão arterial': generate_blood_pressure('high'),
            'Nivel de colesterol': f"{random.randint(200, 300)} mg/dL",
            'Oxigenação': f"{random.randint(85, 95)} %",
            'Nivel de creatinina': f"{round(random.uniform(0.9, 2.0), 1)} mg/dL"
        }
    elif 'normal' in folder_name.lower():
        return {
            'Doença': 'Coração Normal',
            'Descrição': 'Função e estrutura cardíacas normais, eletrocardiograma sem alterações patológicas.',
            'Sintomas': 'Assintomático. Nenhum sintoma.',
            'Tratamento': 'Nenhum tratamento necessário. Recomendação de estilo de vida saúdavel preventivo.',
            'Idade': random.randint(20, 60),
            'Nivel de glicemia': f"{random.randint(70, 99)} mg/dL",
            'Pressão arterial': generate_blood_pressure('normal'),
            'Nivel de colesterol': f"{random.randint(120, 199)} mg/dL",
            'Oxigenação': f"{random.randint(98, 100)} %",
            'Nivel de creatinina': f"{round(random.uniform(0.6, 1.1), 1)} mg/dL"
        }
    elif 'post_mi_history' in folder_name.lower():
        return {
            'Doença': 'Histórico de Infarto do Miocárdio',
            'Descrição': 'Paciente com histórico de infarto prévio, apresentando áreas de tecido cicatricial no coração.',
            'Sintomas': 'Fadiga aos esforços, pode ser assintomático dependendo do nível de reabilitação e dano miocárdico.',
            'Tratamento': 'Controle rigoroso dos fatores de risco (estatinas intensivas, antiplaquetários, IECAs), acompanhamento ambulatorial.',
            'Idade': random.randint(50, 95),
            'Nivel de glicemia': f"{random.randint(85, 130)} mg/dL",
            'Pressão arterial': generate_blood_pressure('normal'), # Usually controlled with meds
            'Nivel de colesterol': f"{random.randint(130, 190)} mg/dL", # Controlled with statins
            'Oxigenação': f"{random.randint(94, 99)} %",
            'Nivel de creatinina': f"{round(random.uniform(0.8, 1.6), 1)} mg/dL"
        }
    else:
        return {
            'Doença': 'Desconhecida',
            'Descrição': 'Condição cardíaca não especificada.',
            'Sintomas': '-',
            'Tratamento': '-',
            'Idade': random.randint(30, 70),
            'Nivel de glicemia': f"{random.randint(70, 120)} mg/dL",
            'Pressão arterial': generate_blood_pressure('normal'),
            'Nivel de colesterol': f"{random.randint(150, 200)} mg/dL",
            'Oxigenação': f"{random.randint(95, 100)} %",
            'Nivel de creatinina': f"{round(random.uniform(0.7, 1.2), 1)} mg/dL"
        }

def main():
    base_dir = r"c:/Users/felip/OneDrive/Documentos/FIAP 2 ano/ex_fase1_5"
    asset_dir = os.path.join(base_dir, "asset")
    output_csv = os.path.join(base_dir, "doencas_cardiacas.csv")

    columns = [
        "Imagem", "Doença", "Descrição", "Sintomas", "Tratamento", 
        "Idade", "Nivel de glicemia", "Pressão arterial", 
        "Nivel de colesterol", "Oxigenação", "Nivel de creatinina"
    ]

    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()

        for folder in os.listdir(asset_dir):
            folder_path = os.path.join(asset_dir, folder)
            if os.path.isdir(folder_path):
                # Retrieve all images inside this directory
                for file_name in os.listdir(folder_path):
                    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
                        rel_path = f"asset/{folder}/{file_name}"
                        disease_data = get_disease_info(folder)
                        row = {'Imagem': rel_path}
                        row.update(disease_data)
                        writer.writerow(row)

    print(f"File {output_csv} generated successfully.")

if __name__ == '__main__':
    main()
