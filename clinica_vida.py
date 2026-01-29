# Lista global para armazenar os pacientes.
# Cada paciente será um dicionário dentro desta lista.
pacientes = []

def cadastrar_paciente():
    """Permite ao usuário cadastrar um novo paciente com nome, idade e telefone."""
    nome = input("Nome do paciente: ")
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida para a idade. Por favor, insira um número inteiro.")
    telefone = input("Telefone: ")
    
    # Cria o dicionário com os dados do paciente
    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    # Adiciona o dicionário à lista global de pacientes
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def ver_estatisticas():
    """Calcula e exibe estatísticas básicas sobre os pacientes cadastrados."""
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    
    total_pacientes = len(pacientes)
    # Extrai todas as idades para uma nova lista usando list comprehension
    idades = [p['idade'] for p in pacientes]
    idade_media = sum(idades) / total_pacientes
    # Encontra o paciente mais novo e mais velho usando a função min/max com uma chave de ordenação (lambda)
    paciente_mais_novo = min(pacientes, key=lambda p: p['idade'])
    paciente_mais_velho = max(pacientes, key=lambda p: p['idade'])
    
    print(f"\nNúmero total de pacientes: {total_pacientes}")
    print(f"Idade média dos pacientes: {idade_media:.2f} anos")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")

def buscar_paciente():
    """Permite buscar um paciente pelo nome (busca parcial e case-insensitive)."""
    nome_busca = input("Digite o nome do paciente para buscar: ")
    encontrados = []
    
    # Itera sobre os pacientes para encontrar correspondências
    for p in pacientes:
        if nome_busca.lower() in p['nome'].lower():
            encontrados.append(p)
            
    if not encontrados:
        print("Nenhum paciente encontrado com este nome.")
    else:
        print("\nPacientes encontrados:")
        for p in encontrados:
            print(f"Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")

def listar_pacientes():
    """Exibe todos os pacientes cadastrados em um formato organizado."""
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    
    print("\n--- LISTA DE PACIENTES ---")
    # Usa enumerate para adicionar um número de item começando do 1
    for i, p in enumerate(pacientes, 1):
        print(f"{i}. Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")

def menu():
    """Função principal que exibe o menu e gerencia a navegação do usuário."""
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            ver_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listar_pacientes()
        elif opcao == '5':
            print("Saindo do sistema...")
            break  # Interrompe o loop while True e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")

# Garante que o menu seja iniciado quando o script Python for executado
if __name__ == "__main__":
    menu()
