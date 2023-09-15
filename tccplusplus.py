import os
import plistlib
import subprocess

def obter_bundle_id(caminho_do_aplicativo):
    caminho_do_info_plist = os.patch.join(caminho_do_aplicativo, "Contents", "Info.plist")