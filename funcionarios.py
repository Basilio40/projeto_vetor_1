import PyPDF2
import tabula
from PyPDF2.pdf import PdfFileReader, PdfFileWriter


#=======================================LENDO DADOS DOS HOLERITES DOS FUNCIONARIOS===================================================
class CarregarPDF:
    def __init__(self):
        self.holerite = r"C:\Users\Sandro Bispo\Desktop\Pythons_do_mes\projeto_vetor\Holerite\HOLERITES 10-2020.pdf"

    def carregaholerite(self):
        self.lerHolerite =  PyPDF2.PdfFileReader(self.holerite)
        self.pagina = self.lerHolerite.getPage(0)
        self.conteudo = self.pagina.extractText()
        print(self.conteudo)
                      
#========================================== LENDO E DIVIDINDO O CARTÃO DE POR FUNCIONARIO ====================================================
    def split_pdf(ponto):
        ponto = PdfFileReader(open(r"C:\Users\Sandro Bispo\Desktop\Pythons_do_mes\projeto_vetor\cartao_ponto\Relatório de Jornada (espelho ponto) (26.10.2021- 02.11.2021).pdf", 'rb'))
        funcionarios = tabula.read_pdf(r"C:\Users\Sandro Bispo\Desktop\Pythons_do_mes\projeto_vetor\cartao_ponto\Relatório de Jornada (espelho ponto) (26.10.2021- 02.11.2021).pdf", pages='all')
        for p in range(ponto.numPages):
            saida = PdfFileWriter()
            saida.addPage(ponto.getPage(p))
            funcionario = funcionarios[p].columns[0:1]
            with open(f"saidaponto/{funcionario[0]}.pdf".replace(':',''), "wb") as saidaStream:
                saida.write(saidaStream)
 
 #===========================================RENOMEANDO OS ARQUIVOS DE PONTOS ========================================================
                
        
    
  
carregar = CarregarPDF()
# carregar.carregaholerite()
carregar.split_pdf()

