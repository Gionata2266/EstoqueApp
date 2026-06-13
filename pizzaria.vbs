Set WshShell = CreateObject("WScript.Shell")

WshShell.Run "cmd /c cd /d ""C:\Users\giona\Desktop\Projetos Git"" && call .venv\Scripts\activate && python main.py", 0, False

WScript.Sleep 2000

WshShell.Run "cmd /c cd /d ""C:\Users\giona\Desktop\Projetos Git"" && call .venv\Scripts\activate && python views\app.py", 0, False