import tabula
import re
import os
from PyPDF2.pdf import PdfFileReader, PdfFileWriter



#=======================================LENDO DADOS DOS HOLERITES DOS FUNCIONARIOS===================================================     
class CarregarPdf:
    def __init__(self):
        pass
    # def carregaholerite(holerites):
    #     holerites = PdfFileReader(open(r"C:\Users\Sandro Bispo\Desktop\Pythons_do_mes\projeto_vetor\Holerite\HOLERITES 10-2020.pdf",'rb'))
    #     f = lambda x: re.sub(r'\/|\\', '', x)
    #     for h in range(holerites.numPages):
    #         saida = PdfFileWriter()
    #         saida.addPage(holerites.getPage(h))
    #         pagina = holerites.getPage(h)
    #         conteudo = pagina.extractText()
    #         if len(re.findall(r'(\d.{3,4})+[0-9]{2,3} - (\w.+)', conteudo)) == 1:
    #             continue
    #         find = re.findall(r'(\d.{3,4})+[0-9]{2,3} - (\w.+)', conteudo)[0][-1]
    #         with open(f"saidaholerite/{f(find)}.pdf", "wb") as saidaStream:
    #             saida.write(saidaStream)

                      
#========================================== LENDO E DIVIDINDO O CARTÃO DE POR FUNCIONARIO ====================================================
    def split_pdf(self, arquivo_entrada):
        ponto = PdfFileReader(open(arquivo_entrada , 'rb'))
        funcionarios = tabula.read_pdf(arquivo_entrada, pages='all')
        for p in range(ponto.numPages):
            saida = PdfFileWriter()
            saida.addPage(ponto.getPage(p))
            funcionario = funcionarios[p].columns[0:1]
            with open(f"saidaponto/{funcionario[0]}.pdf".replace(':',''), "wb") as saidaStream:
                saida.write(saidaStream)
 
 #===========================================RENOMEANDO OS ARQUIVOS DE PONTOS ========================================================
                
        
    
carregar = CarregarPdf()  
# carregar.carregaholerite()
carregar.split_pdf(r'C:\Users\Sandro Bispo\Desktop\Pythons_do_mes\projeto_vetor\cartao_ponto\Relatório de Jornada (espelho ponto) (26.10.2021- 02.11.2021).pdf')

