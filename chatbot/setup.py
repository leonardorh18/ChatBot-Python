import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("chat.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["chatterbot", "chatterbot.traines"],
        include_files = [],
        excludes = []
		
)




setup(
    name = "chat",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
