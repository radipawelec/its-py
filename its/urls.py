from django.urls import path, include
from . import views


urlpatterns = [

    path('post/<int:post_id>', views.post, name='post'),
    path('blog/', views.blog, name='blog'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_request, name='login'),
    # path("logout", views.logout_request, name="logout"),
    # path("add/", views.photo_add, name="photo-add"),
    # path("search/", views.search, name="search"),
    # path("follow/", views.follow, name="follow"),
    # path("contacts/", views.contacts, name="contacts"),
    # path("contact_form/", views.send_message, name="send_message"),
    # path("newsletter/", views.newsletter, name="newsletter"),
    # path("inmails/", views.inmails, name="inmails"),
    # path("inmail/<int:inmail_id>", views.inmail, name="inmail"),
    # path("detail/<int:img_id>", views.detail, name="detail"),
    # path("like/<int:img_id>", views.like, name="like"),


]

