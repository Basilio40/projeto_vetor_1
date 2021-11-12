import PyPDF2
from PyPDF2.pdf import PdfFileReader, PdfFileWriter

class CarregarPDF:
    def __init__(self):
        self.holerite = r"C:\Users\Sandro Bispo\Desktop\projeto_vetor\Holerite\HOLERITES 10-2020.pdf"

    def carregaholerite(self):
        self.lerHolerite =  PyPDF2.PdfFileReader(self.holerite)
        self.pagina = self.lerHolerite.getPage(0)
        self.conteudo = self.pagina.extractText()
        # print(self.conteudo)
        
    
    def split_pdf(ponto):
        ponto = PdfFileReader(open(r"C:\Users\Sandro Bispo\Desktop\projeto_vetor\cartao_ponto\Relatório de Jornada (espelho ponto) (26.10.2021- 02.11.2021).pdf", 'rb'))
        for p in range(ponto.numPages):
            saida = PdfFileWriter()
            saida.addPage(ponto.getPage(p))
            with open("saidaponto/ponto-page%s.pdf" %p, "wb") as saidaStream:
                saida.write(saidaStream)
  
carregar = CarregarPDF()
print(carregar.carregaholerite())
carregar.split_pdf()

