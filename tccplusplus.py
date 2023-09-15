import os
import plistlib
import subprocess

def obter_bundle_id(caminho_do_aplicativo):
    caminho_do_info_plist = os.patch.join(caminho_do_aplicativo, "Contents", "Info.plist")

    if os.path.exists(caminho_do_aplicativo):
        with open(caminho_do_info_plist, 'rb') as arquivo_plist:
            dados_do_plist =  plistlib.load(arquivo_plist)
            obter_bundle_id = dados_do_plist.get("CFBundleIdentifier")
            return obter_bundle_id
        
def listar_aplicativos():
    pasta_de_aplicativos = "/Applications" #padrão applications!
    