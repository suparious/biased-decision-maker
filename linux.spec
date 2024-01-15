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
          [],
          name='biased-decision-maker',
          debug=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          bootloader_ignore_signals=False,
          # On Windows, specify the version information
          # version='versioninfo.txt'  # This line is for Windows builds
          )
