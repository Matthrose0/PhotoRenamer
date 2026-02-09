# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['photo_renamer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL._tkinter_finder',
        'PIL.Image',
        'PIL.ExifTags',
        'win32com',
        'win32com.client',
        'win32gui',
        'win32con',
        'pywintypes',
        'pythoncom',
        'psutil',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PhotoRenamer',
    debug=False,                         # WICHTIG: Für Debugging
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # UPX manchmal problematisch
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                       # WICHTIG: Console an für Fehler
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)