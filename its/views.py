from .models import *
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers

#


def post(request, post_id):
    try:
        post_id = post_id
        post = Blog.objects.get(pk=post_id)
        user = User.objects.get(pk=post.post_author.pk)
        user_ = user.username

        data = {
            "post_id" : post.pk,
            "post_title": post.post_title,
            "post_text": post.post_text,
            "post_author":user_,
            "post_img" : "http://127.0.0.1:8000"+post.post_picture.url,
            "post_img_alt": post.post_picture_alt,

        }
        app_json = json.dumps(data)
        # serialized_object = serializers.serialize('json', [data,])

        return HttpResponse(app_json, content_type='application/json')
    except:
        data = {
            "post_title" : "This post don't exist",
        }
        app_json = json.dumps(data)

        return HttpResponse(app_json, content_type='application/json')


def blog(request):
    posts_list = Blog.objects.all()

    posts= [ ]

    for i in posts_list:
        l = {"id" : i.pk, "title": i.post_title, "body": i.post_text, "tldr":i.post_text[0:60]+"..." , "date":str(i.add_date), "author": str(i.post_author)}
        posts.append(l)

    app_json = json.dumps(posts)
    return HttpResponse(app_json, content_type='application/json')

    # blog_posts = serializers.serialize("json", posts.objects.all())
    # data = {"Blog Posts": blog_posts}
    # return JsonResponse(blog_posts)

    # serialized_object = serializers.serialize('json', [blog_posts,])
    # return HttpResponse(serialized_object, content_type='application/json')
    return HttpResponse("test")


