from tkinter import *

class Gui():
    """Classe que define a interface gráfica da aplicação
    """

    # Criando a janela...
    window = Tk()
    window.wm_title("Cadastro de Livros")

    # Criando variáveis que armazenarão o texto inserido pelo usuário...

    txtNome = StringVar()
    txtAutor = StringVar()
    txtEditora = StringVar()
    txtVolume = StringVar()
    txtAnoDeLancamento = StringVar()
    txtLocalPrateleira = StringVar()
    txtFornecedor = StringVar()
    txtDataEntradaDoLivro = StringVar()
    txtEstoqueMinimo = StringVar()
    txtEstoqueMaximo = StringVar()
    txtEstoqueAtual = StringVar()
    txtPrecoCompra = StringVar()
    txtPrecoVenda = StringVar()

    # Criando os objetos que estarão na janela...

    lblnome = Label(window, text="Nome")
    lblautor = Label(window, text="Autor")
    lbleditora = Label(window, text="Editora")
    lblvolume = Label(window, text="Volume")
    lblanolanc = Label(window, text="Ano")
    lbllocal = Label(window, text="Prateleira")
    lblfornecedor = Label(window, text="Fornecedor")
    lbldataentrada = Label(window, text="Data de entrada do Livro")
    lblestoquemin = Label(window, text="Estoque mínimo")
    lblestoquemax = Label(window, text="Estoque máximo")
    lblestoqueatual = Label(window, text="Estoque atual")
    lblprecocompra = Label(window, text="Preço de compra")
    lblprecovenda = Label(window, text="Preço de Venda")
    entNome = Entry(window, textvariable=txtNome)
    entAutor = Entry(window, textvariable=txtAutor)
    entEditora = Entry(window, textvariable=txtEditora)
    entVolume = Entry(window, textvariable=txtVolume)
    entAnolanc = Entry(window, textvariable=txtAnoDeLancamento)
    entLocal = Entry(window, textvariable=txtLocalPrateleira)
    entFornecedor = Entry(window, textvariable=txtFornecedor)
    entDataEntrada = Entry(window, textvariable=txtDataEntradaDoLivro)
    entEstoqueMin = Entry(window, textvariable=txtEstoqueMinimo)
    entEstoqueMax = Entry(window, textvariable=txtEstoqueMaximo)
    entEstoqueAtual = Entry(window, textvariable=txtEstoqueAtual)
    entPrecoCompra = Entry(window, textvariable=txtPrecoCompra)
    entPrecoVenda = Entry(window, textvariable=txtPrecoVenda)
    listLivros = Listbox(window)
    scrollLivros = Scrollbar(window)
    btnViewAll = Button(window, text="Exibir")
    btnInserir = Button(window, text="Inserir")
    btnDel = Button(window, text="Deletar")
    btnClose = Button(window, text="Fechar")

    # Associando os objetos a grid da janela...
    lblnome.grid(row=1, column=0)
    lblautor.grid(row=2, column=0)
    lbleditora.grid(row=3, column=0)
    lblvolume.grid(row=4, column=0)
    lblanolanc.grid(row=5, column=0)
    lbllocal.grid(row=6, column=0)
    lblfornecedor.grid(row=7, column=0)
    lbldataentrada.grid(row=8, column=0)
    lblestoquemin.grid(row=9, column=0)
    lblestoquemax.grid(row=10, column=0)
    lblestoqueatual.grid(row=11, column=0)
    lblprecocompra.grid(row=12, column=0)
    lblprecovenda.grid(row=13, column=0)
    entNome.grid(row=1, column=1, padx=50, pady=50)
    entAutor.grid(row=2, column=1)
    entEditora.grid(row=3, column=1)
    entVolume.grid(row=4, column=1)
    entAnolanc.grid(row=5, column=1)
    entLocal.grid(row=6, column=1)
    entFornecedor.grid(row=7, column=1)
    entDataEntrada.grid(row=8, column=1)
    entEstoqueMin.grid(row=9, column=1)
    entEstoqueMax.grid(row=10, column=1)
    entEstoqueAtual.grid(row=11, column=1)
    entPrecoCompra.grid(row=12, column=1)
    entPrecoVenda.grid(row=13, column=1)
    listLivros.grid(row=0, column=2, rowspan=14, ipadx = 400)
    scrollLivros.grid(row=0, column=6, rowspan=14)
    btnViewAll.grid(row=14, column=0, columnspan=2)
    btnInserir.grid(row=15, column=0, columnspan=2)
    btnDel.grid(row=16, column=0, columnspan=2)
    btnClose.grid(row=17, column=0, columnspan=2)

    # Associando a Scrollbar com a Listbox...
    listLivros.configure(yscrollcommand=scrollLivros.set)

    scrollLivros.configure(command=listLivros.yview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    # Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()
