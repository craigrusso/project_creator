# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\craig_russo\\SynologyDrive\\SCRIPTS\\project_creator\\project_creator_v.13.py'],
             pathex=['C:\\Users\\craig_russo\\SynologyDrive\\SCRIPTS\\project_creator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='project_creator_v.13',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\craig_russo\\SynologyDrive\\SCRIPTS\\project_creator\\Creator.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='project_creator_v.13')
