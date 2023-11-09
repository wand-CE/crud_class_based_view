from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from core.models import Produto


class IndexView(TemplateView):
    template_name = 'index.html'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'formproduto.html'
    fields = ['categoria', 'nome', 'descricao', 'preco']
    success_url = reverse_lazy('listarprodutos')


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'formproduto.html'
    fields = ['categoria', 'nome', 'descricao', 'preco']
    success_url = reverse_lazy('listarprodutos')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'meusprodutos.html'
    queryset = Produto.objects.all().order_by('nome')
    context_object_name = 'produtos'

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'excluirproduto.html'
    success_url = reverse_lazy('listarprodutos')



