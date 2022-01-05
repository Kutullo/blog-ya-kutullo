from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from article.models import Article ,Comment
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import CommentForm
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from datetime import datetime,date
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User


def article (request):
    articles=Article.published_manager.all()
    return render(request,'articles.html',{'articles':articles})


class AddArticleView (CreateView):
    model=Article
    template_name='add_article.html'
    fields = ('title','slug','snippet','detail_header_image','content',
              'reading_min','status','category','tag' )


    def form_valid (self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    
   
    

class UpdateArticleView (LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Article
    template_name='update_article.html'
    fields = ('title','slug','snippet','detail_header_image','content',
              'reading_min','status','category','tag' )

    def test_func(self):
        post=self.get_object()
        if self.request.user ==post.author:
            return True
        return False

class DeleteArticleView (LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Article
    template_name='delete_article.html'
    fields = '__all__'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user ==post.author:
            return True
        return False
    def get_success_url (self):
        return reverse_lazy ('profile')

def category (request ,cat):
    category_article=Article.objects.filter(category__name=cat)
    return  render(request,'categories.html',{'cat':cat ,'category_article':category_article})

class TagArticleView (ListView):
    model = Article
    template_name = 'tags.html'
    context_object_name= 'articles'

    def get_queryset (self):
        return Article.objects.filter(tag__slug=self.kwargs.get('article_tag'))

    def get_context_data(self, **kwargs):
        context = super(TagArticleView, self).get_context_data(**kwargs)
        tag_name =self.kwargs.get('article_tag')
        context['tag'] =tag_name.capitalize()
        return context



class AddCommentView (CreateView):
    model= Comment
    template_name='add_comment.html'
    fields = '__all__'


def detailview (request ,slug_text):
    article_object=Article.objects.filter(slug=slug_text)

    if article_object.exists():
        article_object=article_object.first()
    else :
        return HttpResponse ("<h1>Page not found</h1>")

    if request.method =='POST':

        comment_form=CommentForm(request.POST)

        if comment_form.is_valid():
            user_comment=comment_form.save(commit=False)
            user_comment.post=article_object
            user_comment.save()

            return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else :
        comment_form=CommentForm()



    return  render(request,'article_detail.html',{'article':article_object,'comment_form':comment_form})