#SAIDAS
BotCumprimentos = ['olaaaaaa :D', 'ola', 'oi', 'oiiiiii ', 'Bem vindo S2']

# ENTRADAS
    #Comandos:
ComandAProva = ['addProva', 'addP', 'addp']
Cumprimentos = ['oi', 'Oi', 'ola', 'Ola', 'olaa', 'oii', 'bo dia']
ComandClima = ['tempo', 'Tempo', 'temperatura', 'Temperatura', 'temp']
ComandCota = ['Cotação', 'cotação', 'dolar', 'Dolar']
ComandVProvas = ['verP', 'ver Provas', 'verprovas']
ComandGPT = ['chatgpt', 'ChatGPT', 'chatGPT', 'GPT', 'gpt', 'chat gpt']
ComandAComando = ['Acomando', 'adicionar comando', 'AddComando', 'AddComnad']

    #Vocabulario:
sim = ['Sim', 'SIM', 'S', 's']
nao = ['Não', 'nao', 'não', 'Nao', 'NAo', 'NÃO']

Dicionario_Comandos = {
    'Comandos Adicionar Prova': ComandAProva,
    'Comandos Ver as Provas': ComandVProvas,
    'Comandos Clima': ComandClima,
    'Comandos Cotação': ComandCota,
    'Cumprimentos do Bot': BotCumprimentos,
    'Cumprimentos Usuário': Cumprimentos,
    'Comandos ChatGPT': ComandGPT,
    'Comandos Adicionar Comandos': ComandAComando,
}

for Comandos in Dicionario_Comandos:
    comandos = Dicionario_Comandos[Comandos]
    print(comandos)