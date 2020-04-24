#pip install schedule
import schedule 
import time

def TarefaCadaDezSegundos():
	print('Realizando tarefa')


def TarefaTodaSexta():
	print('Olá bom dia, hoje é sexta-feira')

def TarefaTodaSegundaOitoHoras():
	print('Sei que toda segunda é triste mas temos que trabalhar')

def TarefaTodaDiaSeteoHoras():
	print('bora acordar pra trabaia')

def ModulosSchedule():
	#schedule.a-cada.tempo.faça
	schedule.every(10).secounds.do(TarefaCadaDezSegundos)
	#schedule.a-cada.sexta.faça
	schedule.every().friday.do(TarefaTodaSexta)
	#schedule.a-cada.segunda.as.faça
	schedule.every().monday.at('08:00').do(TarefaTodaSegundaOitoHoras)
	#schedule.todo.dia.as.faça
	schedule.every().day.at('08:00').do(TarefaTodaDiaSeteoHoras)

while True:
	#Roda todas as tarefas
	ModulosSchedule()
	schedule.run_pending()
