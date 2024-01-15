# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['biased-decision-maker.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             noarchive=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          name='biased-decision-maker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          argv_emulation=False,
          target_arch=None,
          codesign_identity=None,  # Add your signing identity or leave None
          entitlements_file=None  # Add path to entitlements file if needed
          )

# TODO: Set an icon, replace 'icon=None' with 'icon='path/to/icon.icns''
app = BUNDLE(exe,
              name='biased-decision-maker.app',
              icon=None,  # Path to the .icns file
              bundle_identifier='net.solidrust.biaseddecisionmaker'
              )
