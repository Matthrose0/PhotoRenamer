# -*- mode: python ; coding: utf-8 -*-
# Build: pyinstaller PhotoRenamer.spec

a = Analysis(
    ['photo_renamer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL._tkinter_finder',
        'win32com',
        'win32com.client',
        'win32gui',
        'win32process',
        'pywintypes',
        'pythoncom',
        'psutil',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PhotoRenamer',
    icon='icon.ico',
    debug=False,    # fuer Fehlersuche auf True setzen
    console=False,  # fuer Fehlersuche auf True setzen
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
