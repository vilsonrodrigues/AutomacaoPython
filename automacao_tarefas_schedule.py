#pip install schedule
import schedule 
import time

def tarefaCadaDezSegundos():
	print('Realizando tarefa')

def tarefaTodaSexta():
	print('Olá bom dia, hoje é sexta-feira')

def tarefaTodaSegundaOitoHoras():
	print('Sei que toda segunda é triste mas temos que trabalhar')

def tarefaTodaDiaSeteoHoras():
	print('bora acordar pra trabaia')

def modulosSchedule():
	#schedule.a-cada.tempo.faça
	schedule.every(10).seconds.do(tarefaCadaDezSegundos)
	#schedule.a-cada.sexta.faça
	schedule.every().friday.do(tarefaTodaSexta)
	#schedule.a-cada.segunda.as.faça
	schedule.every().monday.at('08:00').do(tarefaTodaSegundaOitoHoras)
	#schedule.todo.dia.as.faça
	schedule.every().day.at('08:00').do(tarefaTodaDiaSeteoHoras)

while True:
	#Roda todas as tarefas
	modulosSchedule()
	schedule.run_pending()
