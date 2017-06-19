import pymsgbox
import time
import webbrowser

qtd_min_trab = pymsgbox.prompt("Digite quantos minutos durarao sua sessão de trabalho:", "Tempo de trabalho")
qtd_intervalos = pymsgbox.prompt("Digite quantos intervalos quer fazer:", "Quantidade de intervalos")
qtd_min_intervalo = pymsgbox.prompt("Digite o quantos minutos durarão seu intervalo:", "Duração do intervalo")

""" MELHORIA: definir tempo mínimo de trabalho """
qtd_min_pre_intervalo = int(qtd_min_trab) - 5

contador_intervalos = 1

pymsgbox.alert(text="Hora de início do programa: "+time.ctime(), title="Break time")

"""	enquanto o programa ainda não atingiu a quantidade de intervalos proposta pelo usuário """
while int(contador_intervalos) <= int(qtd_intervalos):
	""" coloca o programa para aguardar o tempo informado pelo usuário
	    (qtd_min_pre_intervalo * 60) """
	time.sleep(5)
	pymsgbox.alert(text="Faltam 5 minutos para o seu intervalo", title="Atenção!")
	""" 5 minutos antes do intervalo, avisa o usuário
	    5 minutos (5 * 60) """
	time.sleep(5)
	""" Avisa que chegou a hora do intervalo """
	pymsgbox.alert(text="Hora do intervalo", title="Atenção")
	""" abre o video do youtube """
	webbrowser.open("https://www.youtube.com/watch?v=DLHAiojuUq0")
	""" coloca o programa para aguardar o tempo do intervalo """
	time.sleep(int(qtd_min_intervalo))
	""" se a quantidade de intervalos ainda não atingiu o total informado pelo usuário """
	if int(contador_intervalos) < int(qtd_intervalos) :
		pymsgbox.alert(text="Agora voltemos ao trabalho!", title="Aviso")
	else :
		pymsgbox.alert(text="Ótimo! por hoje chega :)", title="Agora vá descansar :)")
	contador_intervalos = contador_intervalos + 1
