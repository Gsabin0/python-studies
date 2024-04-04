import subprocess

# Esta classe pode ser usada com  a plataforma do Antoniel.

cmd = ['ping', '172.27.144.1']

proc = subprocess.run(cmd)

print(proc.returncode) # pode ser usado pra achar erros 