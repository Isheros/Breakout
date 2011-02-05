# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'),
              os.path.join(HOMEPATH,'support\\useUnicode.py'),
              'C:\\Development\\Python\\Breakout\\src\\main.py'],
              pathex=['C:\\pyinstaller',])

pyz = PYZ(a.pure,name=os.path.join('','data.pyz'),level=9)

exe = EXE(pyz,
          a.scripts+ [('O','','OPTION')],
          exclude_binaries=1,
          name=os.path.join('bin\\build\\', 'Breakout.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('bin', 'dist'))