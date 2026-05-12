import random
import time
import os

# Configurações de armazenamento (Constants)
PRIMARY_STORAGE = "dados_primarios.txt"
BACKUP_STORAGE = "backup.txt"

def simulate_sensor_data():
    """Simula a leitura de três sensores distintos."""
    return {
        "temperature": random.randint(20, 30),
        "humidity": random.randint(40, 70),
        "luminosity": random.randint(100, 500),
        "timestamp": time.strftime('%H:%M:%S')
    }

def save_to_file(file_path, data):
    """Encapsula a lógica de escrita em arquivo."""
    try:
        with open(file_path, "a") as file:
            file.write(data + "\n")
        return True
    except IOError:
        return False

def gateway_processor(sensor_payload):
    """
    Atua como Gateway: Formata os dados e realiza a 
    replicação total em dois nós de armazenamento.
    """
    formatted_data = (
        f"[{sensor_payload['timestamp']}] "
        f"Temp: {sensor_payload['temperature']}C, "
        f"Umid: {sensor_payload['humidity']}%, "
        f"Lumi: {sensor_payload['luminosity']}lx"
    )

    # Replicação em múltiplos destinos
    save_to_file(PRIMARY_STORAGE, formatted_data)
    save_to_file(BACKUP_STORAGE, formatted_data)
    
    print(f"Dados processados e replicados: {formatted_data}")

def get_system_data():
    """
    Tenta ler do armazenamento principal. Em caso de falha, 
    ativa o mecanismo de redundância (Failover) para o backup.
    """
    target_storage = PRIMARY_STORAGE

    if not os.path.exists(target_storage):
        print(f"Falha detectada: {PRIMARY_STORAGE} inacessivel.")
        print(f"Redirecionando leitura para: {BACKUP_STORAGE}")
        target_storage = BACKUP_STORAGE

    try:
        with open(target_storage, "r") as file:
            last_entry = file.readlines()[-1].strip()
            return f"Sucesso ao ler de {target_storage}: {last_entry}"
    except (IndexError, FileNotFoundError):
        return "Erro: Nenhum dado disponível em ambos os sistemas."

def run_simulation():
    """Execução principal do fluxo de dados e teste de resiliência."""
    
    print("--- Fase 1: Coleta e Replicacao ---")
    for _ in range(3):
        data = simulate_sensor_data()
        gateway_processor(data)
        time.sleep(1)

    print("\n--- Fase 2: Teste de Resiliencia ---")
    # Para testar a falha, o arquivo principal deve ser removido manualmente
    # ou via código como na linha abaixo:
    # os.remove(PRIMARY_STORAGE)
    
    result = get_system_data()
    print(result)

if __name__ == "__main__":
    run_simulation()