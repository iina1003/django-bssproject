from django.shortcuts import render
from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from .forms import SearchForm       # forms.pyからsearchFormクラスをインポート
class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'

class DetailView(generic.DetailView):  # ← 修正済み
    model = Article
    template_name = 'bbs/detail.html'

# CreateViewクラスを作成
class CreateView(generic.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

# UpdateViewクラスを作成
class UpdateView(generic.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'
    
class DeleteView(generic.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')
    


# 検索機能のビュー
def search(request):
  articles = None # 検索結果を格納する変数を初期化
  searchform = SearchForm(request.GET) # GETリクエストで送信したデータが格納される（詳細は解説にて）
    
  # Formに正常なデータがあれば
  if searchform.is_valid():
   query = searchform.cleaned_data['words']   # queryにフォームが持っているデータを代入
   articles = Article.objects.filter(content__icontains=query)    # クエリを含むレコードをfilterメソッドで取り出し、articles変数に代入
   return render(request, 'bbs/results.html', {'articles':articles,'searchform':searchform})