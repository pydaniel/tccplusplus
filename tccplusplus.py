import os
import plistlib
import subprocess

#por @pydaniel 

def obter_bundle_id(caminho_do_aplicativo):
    caminho_do_info_plist = os.patch.join(caminho_do_aplicativo, "Contents", "Info.plist")

    if os.path.exists(caminho_do_aplicativo):
        with open(caminho_do_info_plist, 'rb') as arquivo_plist:
            dados_do_plist =  plistlib.load(arquivo_plist)
            obter_bundle_id = dados_do_plist.get("CFBundleIdentifier")
            return obter_bundle_id
        
def listar_aplicativos():
    pasta_de_aplicativos = "/Applications" #padrão applications!
    
    if os.path.exists(pasta_de_aplicativos):
        lista_de_aplicativos = []
        for idx, nome_do_aplicativo  in enumerate(os.listdir(pasta_de_aplicativos), start=1):
            caminho_do_aplicativo = os.path.join(pasta_de_aplicativos, nome_do_aplicativo)

            if os.path.isdir(caminho_do_aplicativo):
                bundle_id = obter_bundle_id(caminho_do_aplicativo)
                if bundle_id:
                    lista_de_aplicativos.append((idx, nome_do_aplicativo, bundle_id))

print("Lista de Aplicativos:")
for idx, nome_do_aplicativo, obter_bundle_id in listar_aplicativos:
    print(f"{idx}. Aplicativo: {nome_do_aplicativo} - Bundle ID: {obter_bundle_id}")

entrada_do_usuario = input("Escolha o número do aplicativo ou digite o ID: ")
aplicativo_selecionado = None

for app in lista_de_aplicativos:
        if entrada_do_usuario.isdigit():
                if int(entrada_do_usuario) == app[0]:
                    aplicativo_selecionado = app
                    break
        elif entrada_do_usuario == app[2]:
                aplicativo_selecionado = app
                break

        if aplicativo_selecionado:
            print(f"Você escolheu: {aplicativo_selecionado[1]} - Bundle ID: {aplicativo_selecionado[2]}")

            servicos_disponiveis = [
                "All", "Accessibility", "AddressBook", "AppleEvents", "Calendar", "Camera", "ContactsFull",
                "ContactsLimited", "DeveloperTool", "Facebook", "LinkedIn", "ListenEvent", "Liverpool", "Location",
                "MediaLibrary", "Microphone", "Motion", "Photos", "PhotosAdd", "PostEvent", "Reminders",
                "ScreenCapture", "ShareKit", "SinaWeibo", "Siri", "SpeechRecognition", "SystemPolicyAllFiles",
                "SystemPolicyDesktopFolder", "SystemPolicyDeveloperFiles", "SystemPolicyDocumentsFolder",
                "SystemPolicyDownloadsFolder", "SystemPolicyNetworkVolumes", "SystemPolicyRemovableVolumes",
                "SystemPolicySysAdminFiles", "TencentWeibo", "Twitter", "Ubiquity", "Willow"
            ]

            print("Serviços disponíveis:")
            for idx, servico in enumerate(servicos_disponiveis, start=1):
                print(f"{idx}. {servico}")

            escolhas = input(
                "Digite o número do serviço que deseja conceder: ")
            escolhas = escolhas.split(',')
            escolhas = [int(escolha.strip()) for escolha in escolhas if escolha.strip().isdigit()]

            servicos_selecionados = [servicos_disponiveis[idx - 1] for idx in escolhas if
                                     1 <= idx <= len(servicos_disponiveis)]

            if servicos_selecionados:
                comando = f"./tccplus add {' '.join(servicos_selecionados)} {aplicativo_selecionado[2]}"
                subprocess.run(comando, shell=True)
                print("Permissões adicionadas com sucesso.")
            else:
                print("Nenhuma permissão selecionada.")
        else:
            print(
                "Número de aplicativo ou Bundle ID inválido. Deve escolher um número na lista ou fornecer um Bundle ID válido.")
else:
        print("A pasta de aplicativos não foi encontrada.")


if __name__ == "__main__":
    listar_aplicativos()
