#Bibliotecas necessarias para uso
import customtkinter as ctk
from src.database import DataBase as db
from src.utils import gen_id, gen_privete_key
import pandas as pd


# Função para simular a navegação
def show_page(page_name):
    # Oculta todas as "páginas"
    for widget in root.winfo_children():
        widget.grid_forget()

    # Exibe a página selecionada
    if page_name == "menu":
        show_menu()
    elif page_name == "cadastro_usuario":
        show_cadastro_usuario()
    elif page_name == "cadastro_oferta":
        show_cadastro_oferta()
    elif page_name == "buscar_carona":
        show_buscar_carona()
    elif page_name == "ajuda":
        show_ajuda()
    elif page_name == "sair":
        root.destroy()  # Encerra o programa

# Função para mostrar o menu principal
def show_menu():
    frame_1 = ctk.CTkFrame(master=root, fg_color="#DCDCDC")
    frame_1.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)  # Ajuste de padding para a borda

    ctk.CTkLabel(master=frame_1, text="Menu", font=("Arial Bold", 20), justify="center").pack(expand=True, pady=[20, 50])

    # Botões clicáveis no menu
    button_cadastrar_usuario = ctk.CTkButton(master=frame_1, text="[1] Cadastrar usuário", command=lambda: show_page("cadastro_usuario"))
    button_cadastrar_usuario.pack(expand=True, pady=20)

    button_cadastrar_oferta = ctk.CTkButton(master=frame_1, text="[2] Cadastrar Oferta de carona", command=lambda: show_page("cadastro_oferta"))
    button_cadastrar_oferta.pack(expand=True, pady=20)

    button_buscar_carona = ctk.CTkButton(master=frame_1, text="[3] Buscar carona", command=lambda: show_page("buscar_carona"))
    button_buscar_carona.pack(expand=True, pady=20)

    button_ajuda = ctk.CTkButton(master=frame_1, text="[4] Ajuda", command=lambda: show_page("ajuda"))
    button_ajuda.pack(expand=True, pady=20)

    button_sair = ctk.CTkButton(master=frame_1, text="[0] Sair", command=lambda: show_page("sair"))
    button_sair.pack(expand=True, pady=20)
    
# Verificar se a base de dados existe, se não existe, cria
path = '.\\data\\'
if db.exist_database(path) == True:
    pass
else:
    db.creat_database(path)

# Abrir os arquivos de dados
path_dim_user = '.\\data\\dim_user.parquet'
dim_user = pd.read_parquet(path_dim_user)

path_fact_ride = '.\\data\\fact_ride.parquet'
fact_ride = pd.read_parquet(path_fact_ride)


# Função para mostrar a página de cadastro de usuário
def show_cadastro_usuario():
    frame = ctk.CTkFrame(master=root)
    frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

    label = ctk.CTkLabel(master=frame, text="Cadastro de Usuário", font=("Arial", 20))
    label.pack(pady=20)

    name_label = ctk.CTkLabel(master=frame, text="Nome:")
    name_label.pack(pady=10)
    name_entry = ctk.CTkEntry(master=frame)
    name_entry.pack(pady=10)

    email_label = ctk.CTkLabel(master=frame, text="Email:")
    email_label.pack(pady=10)
    email_entry = ctk.CTkEntry(master=frame)
    email_entry.pack(pady=10)

    phone_label = ctk.CTkLabel(master=frame, text="Telefone:")
    phone_label.pack(pady=10)
    phone_entry = ctk.CTkEntry(master=frame)
    phone_entry.pack(pady=10)

    local_label = ctk.CTkLabel(master=frame, text="Região Administrativa:")
    local_label.pack(pady=10)
    local_entry = ctk.CTkEntry(master=frame)
    local_entry.pack(pady=10)

    def cadastrar_usuario():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        local = local_entry.get()

        idd = gen_id(dim_user['id'])
        private_key = gen_privete_key(dim_user['private_key'])

        user = {'id': idd, 'name': name, 'email': email, 'phone': phone, 'local': local, 'private_key': private_key}
        user_append = pd.Series(user)

        dim_user = pd.concat([dim_user, user_append.to_frame().T], ignore_index=True)
        print(f"Usuário {name} cadastrado com sucesso! Sua chave privada é: {private_key}")

    cadastro_button = ctk.CTkButton(master=frame, text="Cadastrar", command=cadastrar_usuario)
    cadastro_button.pack(pady=20)

    button_voltar = ctk.CTkButton(master=frame, text="Voltar", command=lambda: show_page("menu"))
    button_voltar.pack(pady=20)


# Função para mostrar a página de cadastro de oferta
def show_cadastro_oferta():
    frame = ctk.CTkFrame(master=root)
    frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

    label = ctk.CTkLabel(master=frame, text="Cadastro de Oferta de Carona", font=("Arial", 20))
    label.pack(pady=20)

    # Campos para origem e destino
    local_origin_label = ctk.CTkLabel(master=frame, text="Origem:")
    local_origin_label.pack(pady=10)
    local_origin_entry = ctk.CTkEntry(master=frame)
    local_origin_entry.pack(pady=10)

    local_dest_label = ctk.CTkLabel(master=frame, text="Destino:")
    local_dest_label.pack(pady=10)
    local_dest_entry = ctk.CTkEntry(master=frame)
    local_dest_entry.pack(pady=10)

    # Data e horário
    datatime_label = ctk.CTkLabel(master=frame, text="Data e Hora (DD-MM-YY HH:MM):")
    datatime_label.pack(pady=10)
    datatime_entry = ctk.CTkEntry(master=frame)
    datatime_entry.pack(pady=10)

    def cadastrar_oferta():
        local_origin = local_origin_entry.get()
        local_dest = local_dest_entry.get()
        datatime = datatime_entry.get()

        idd = gen_id(fact_ride['id'])
        user_id = 1  # Isso deve ser obtido com base na autenticação (como no código original)

        offer = {'id': idd, 'user_id': user_id, 'local_origin': local_origin, 'local_destination': local_dest, 'datatime': pd.to_datetime(datatime)}
        offer_append = pd.Series(offer)

        fact_ride = pd.concat([fact_ride, offer_append.to_frame().T], ignore_index=True)
        print(f"Oferta de carona cadastrada de {local_origin} para {local_dest} às {datatime}.")

    cadastro_button = ctk.CTkButton(master=frame, text="Cadastrar Oferta", command=cadastrar_oferta)
    cadastro_button.pack(pady=20)

    button_voltar = ctk.CTkButton(master=frame, text="Voltar", command=lambda: show_page("menu"))
    button_voltar.pack(pady=20)


# Função para mostrar a página de busca de carona
def show_buscar_carona():
    frame = ctk.CTkFrame(master=root)
    frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

    label = ctk.CTkLabel(master=frame, text="Buscar Carona", font=("Arial", 20))
    label.pack(pady=20)

    # Campos de entrada
    local_origin_label = ctk.CTkLabel(master=frame, text="Origem:")
    local_origin_label.pack(pady=10)
    local_origin_entry = ctk.CTkEntry(master=frame)
    local_origin_entry.pack(pady=10)

    local_dest_label = ctk.CTkLabel(master=frame, text="Destino:")
    local_dest_label.pack(pady=10)
    local_dest_entry = ctk.CTkEntry(master=frame)
    local_dest_entry.pack(pady=10)

    datatime_label = ctk.CTkLabel(master=frame, text="Data e Hora Inicial (DD-MM-YY HH:MM):")
    datatime_label.pack(pady=10)
    datatime_entry = ctk.CTkEntry(master=frame)
    datatime_entry.pack(pady=10)

    def buscar_carona():
        local_origin = local_origin_entry.get()
        local_dest = local_dest_entry.get()
        datatime = datatime_entry.get()

        # Implementar a busca aqui
        print(f"Buscando carona de {local_origin} para {local_dest} após {datatime}.")
    
    buscar_button = ctk.CTkButton(master=frame, text="Buscar", command=buscar_carona)
    buscar_button.pack(pady=20)

    button_voltar = ctk.CTkButton(master=frame, text="Voltar", command=lambda: show_page("menu"))
    button_voltar.pack(pady=20)


# Função para mostrar a página de ajuda
def show_ajuda():
    frame = ctk.CTkFrame(master=root)
    frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

    label = ctk.CTkLabel(master=frame, text="Página de Ajuda", font=("Arial", 20))
    label.pack(pady=20)

    button_voltar = ctk.CTkButton(master=frame, text="Voltar", command=lambda: show_page("menu"))
    button_voltar.pack(pady=20)

# Configurando a janela principal
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Criando a janela principal
root = ctk.CTk()
root.title("Projeto Caronas")

# Definindo o tamanho da janela 
root.geometry(f"800x800")

# Configurar o grid para a janela
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciando a interface com o menu principal
show_page("menu")

# Rodando o loop da interface
root.mainloop()
