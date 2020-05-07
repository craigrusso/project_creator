# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/craigrusso/SynologyDrive/SCRIPTS/project_creator/project_creator_v.13mac.py'],
             pathex=['/Users/craigrusso/SynologyDrive/SCRIPTS/project_creator'],
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
          name='project_creator_v.13mac',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='/Users/craigrusso/SynologyDrive/SCRIPTS/project_creator/Creator.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='project_creator_v.13mac')
app = BUNDLE(coll,
             name='project_creator_v.13mac.app',
             icon='/Users/craigrusso/SynologyDrive/SCRIPTS/project_creator/Creator.ico',
             bundle_identifier=None)
