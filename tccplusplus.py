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

for app in listar_aplicativos:
    if entrada_do_usuario.isdigit():
        if int(entrada_do_usuario) == app[0]:
            aplicativo_selecionado = app
            break
    elif entrada_do_usuario == app[2]:
        aplicativo_selecionado = app
    break


if __name__ == "__main__":
    listar_aplicativos()