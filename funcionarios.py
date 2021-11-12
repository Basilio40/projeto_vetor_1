import PyPDF2
import tabula
from PyPDF2.pdf import PdfFileReader, PdfFileWriter

#=======================================LENDO DADOS DOS HOLERITES DOS FUNCIONARIOS===================================================
class CarregarPDF:
    def __init__(self):
        self.holerite = r"C:\Users\Sandro Bispo\Desktop\projeto_vetor\Holerite\HOLERITES 10-2020.pdf"

    def carregaholerite(self):
        self.lerHolerite =  PyPDF2.PdfFileReader(self.holerite)
        self.pagina = self.lerHolerite.getPage(0)
        self.conteudo = self.pagina.extractText()
        # print(self.conteudo)
        
#========================================== DIVIDINDO O CARTÃO DE POR FUNCIONARIO ====================================================
    def split_pdf(ponto):
        ponto = PdfFileReader(open(r"C:\Users\Sandro Bispo\Desktop\projeto_vetor\cartao_ponto\Relatório de Jornada (espelho ponto) (26.10.2021- 02.11.2021).pdf", 'rb'))
        for p in range(ponto.numPages):
            saida = PdfFileWriter()
            saida.addPage(ponto.getPage(p))
            with open("saidaponto/ponto-page%s.pdf" %p, "wb") as saidaStream:
                saida.write(saidaStream)
                
#======================================= LENDO OS DADOS DO CARTÃO DE PONTO ===========================================================              
    def read_ponto(self):
        self.funcionario = tabula.read_pdf(r"C:\Users\Sandro Bispo\Desktop\projeto_vetor\saidaponto\ponto-page0.pdf", pages='all')
        print(self.funcionario)
  
carregar = CarregarPDF()
carregar.carregaholerite()
carregar.split_pdf()
carregar.read_ponto()
