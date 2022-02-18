from django.http import JsonResponse
from blog.models import Comments, Articles


def index(request):
    titles = []
    for comment in Comments.objects.all():
        titles.append(comment.article.title)
    return JsonResponse({"titles": list(set(titles))})


def index_for_efficient_way(request):
    titles = []
    for comment in Comments.objects.select_related('article').all():
        titles.append(comment.article.title)
    return JsonResponse({"titles": list(set(titles))})


def comments(request):
    tmp_comments = []
    for article in Articles.objects.all():
        for row_comment in article.comments_set.all():
            tmp_comments.append(row_comment.comment)
    return JsonResponse({"Comments": list(set(tmp_comments))})


def efficient_comments(request):
    tmp_comments = []
    for article in Articles.objects.prefetch_related('comments_set').all():
        for row_comment in article.comments_set.all():
            tmp_comments.append(row_comment.comment)
    return JsonResponse({"Comments": list(set(tmp_comments))})
