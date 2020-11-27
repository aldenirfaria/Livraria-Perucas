#Desenvolvido pelo time Aldenir Faria, Gabriel e Kleber
#atualizado por Aldenir Faria dia 27/11/2020
#obrigado professor!!!!

from GUI import *
import Backend as core


app = None

def view_command():
    rows = core.view()
    app.listLivros.delete(0, END)
    for r in rows:
        app.listLivros.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtAutor.get(), app.txtEditora.get(), app.txtVolume.get(), app.txtAnoDeLancamento.get(), app.txtLocalPrateleira.get(), app.txtFornecedor.get(), app.txtDataEntradaDoLivro.get(), app.txtEstoqueMinimo.get(), app.txtEstoqueMaximo.get(), app.txtEstoqueAtual.get(), app.txtPrecoCompra.get(), app.txtPrecoVenda.get())
    view_command()


def del_command():
    li_codigo = selected[0]
    core.delete(li_codigo)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listLivros.curselection()[0]
    selected = app.listLivros.get(index)
    app.entNome.insert(END, selected[1])
    app.entNome.delete(0, END)
    app.entAutor.insert(END, selected[2])
    app.entAutor.delete(0, END)
    app.entEditora.insert(END, selected[3])
    app.entEditora.delete(0, END)
    app.entVolume.insert(END, selected[4])
    app.entVolume.delete(0, END)
    app.entAnolanc.insert(END, selected[5])
    app.entAnolanc.delete(0, END)
    app.entLocal.insert(END, selected[6])
    app.entLocal.delete(0, END)
    app.entFornecedor.insert(END, selected[7])
    app.entFornecedor.delete(0, END)
    app.entDataEntrada.insert(END, selected[8])
    app.entDataEntrada.delete(0, END)
    app.entEstoqueMin.insert(END, selected[9])
    app.entEstoqueMin.delete(0, END)
    app.entEstoqueMax.insert(END, selected[10])
    app.entEstoqueMax.delete(0, END)
    app.entEstoqueAtual.insert(END, selected[11])
    app.entEstoqueAtual.delete(0, END)
    app.entPrecoCompra.insert(END, selected[12])
    app.entPrecoCompra.delete(0, END)
    app.entPrecoVenda.insert(END, selected[13])
    app.entPrecoVenda.delete(0, END)
    return selected


if __name__ == "__main__":
    app = Gui()
    app.listLivros.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnInserir.configure(command=insert_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
