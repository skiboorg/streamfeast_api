from django.urls import path
from . import views

urlpatterns = [
    path('get_streamers', views.GetStreamers.as_view()),
    path('get_streamer', views.GetStreamer.as_view()),
    path('get_faq', views.GetFaq.as_view()),
    path('get_how_to', views.GetHowTo.as_view()),
    path('get_tickets', views.GetTickets.as_view()),
    path('get_cart', views.GetCart.as_view()),
    path('add_item', views.AddItem.as_view()),
     path('change_item_quantity', views.ChangeItemQuantity.as_view()),
    # path('add_item_quantity', views.AddItemQuantity.as_view()),
    # path('delete_item_quantity', views.DeleteItemQuantity.as_view()),
    path('delete_item', views.DeleteItem.as_view()),
    path('save_user_data', views.SaveUserData.as_view()),
    path('get_user_data', views.GetUserData.as_view()),
    path('create_order', views.CreateOrder.as_view()), 
    path('get_ticket', views.GetTicket.as_view()),
    path('subscribe_email', views.SubscribeEmail.as_view()),
]
