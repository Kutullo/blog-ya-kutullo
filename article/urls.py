from django.urls import  path
from article import views
from  .views import AddArticleView,UpdateArticleView,TagArticleView,AddCommentView,DeleteArticleView

urlpatterns = [
    path ('',views.article ,name='article'),
    path ('add_article/',AddArticleView.as_view(),name='add_article'),
    path ('edit/<slug:slug>',UpdateArticleView.as_view(),name='update_article'),
    path ('delete/<slug:slug>',DeleteArticleView.as_view(),name='delete_article'),
    path  ('category/<str:cat>/',views.category,name='category'),
    path  ('tag/<slug:article_tag>/',TagArticleView.as_view(),name='tag_slug'),
    path ('<int:pk>/comment/',AddCommentView.as_view(),name='add_comment'),
    path ('<slug:slug_text>',views.detailview,name='article_details')

    ]