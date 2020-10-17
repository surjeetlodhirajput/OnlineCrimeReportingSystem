from cx_Freeze import *
includefiles=['1.ico']
base=None
if sys.platform=='win32':
    base='Win32GUI'
shortcut_table=[
    ('DesktopShortcut',#shortcut
     'DesktopFolder',#Directory
     'OnlineCrimeReportingSystem',#Name
     'TARGETDIR',#components
     "[TARGETDIR]\OnlineCrimeReportingSystem.exe",#Target
     None,#agrguments
     None,#Description
     None,#Hotkey
     None,#Icon
     None,#IconIndex
     None,#Showsmd
     "TARGETDIR",#WkDir

    )
]
msi_data={'Shortcut':shortcut_table}
#change some default MSI Option and specify the use of the above define table
bdist_msi_options={'data':msi_data}
setup(
    version='0.1',
    description='Online Crime Reporting System',
    author='Surjeet & Anwar',
    name="OnlineCrimeReportingSystem",
    options={'build_exe':{'include_files':includefiles},'bdsit_msi':bdist_msi_options,},
    executables=[
        Executable(
            script='__init__.py',
            base=base,
            icon='1.ico'

        )
    ]
)
