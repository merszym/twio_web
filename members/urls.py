from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="member_index"),
    path("get-sessions", views.get_training_section, name="get_training_section"),
    path(
        "veranstaltungen/<int:pk>/",
        views.EventDetailView.as_view(),
        name="event_detail",
    ),
    path("veranstaltungen/neu/", views.EventCreateView.as_view(), name="event_create"),
    path(
        "veranstaltungen/<int:pk>/ändern/",
        views.EventUpdateView.as_view(),
        name="event_update",
    ),
    path(
        "veranstaltungen/<int:pk>/löschen/",
        views.EventDeleteView.as_view(),
        name="event_delete",
    ),
    path(
        "veranstaltungen/<int:pk>/teilnehmen/",
        views.EventParticipateView.as_view(),
        name="event_participate",
    ),
    path(
        "veranstaltungen/<int:pk>/orga/",
        views.EventOrgaView.as_view(),
        name="event_participants",
    ),
    path(
        "veranstaltungen/<int:pk>/stornieren/",
        views.EventUnParticipateView.as_view(),
        name="event_unparticipate",
    ),
    path(
        "veranstaltungen/ajax/update_participant/",
        views.update_memberparticipant,
        name="ajax_update_memberparticipant",
    ),
    path(
        "veranstaltungen/ajax/update_file/",
        views.ajax_event_filehandle,
        name="ajax_event_filehandle",
    ),
    path(
        "trainingseinheit/<int:pk>/",
        views.SessionDetailView.as_view(),
        name="session_detail",
    ),
    path(
        "trainingseinheit/neu/",
        views.SessionCreateView.as_view(),
        name="session_create",
    ),
    path(
        "trainingseinheit/<int:pk>/ändern/",
        views.SessionUpdateView.as_view(),
        name="session_update",
    ),
    path(
        "trainingseinheit/<int:pk>/löschen/",
        views.SessionDeleteView.as_view(),
        name="session_delete",
    ),
    path("spots/", views.SpotListView.as_view(), name="spot_list"),
    path("spots/<int:pk>/", views.SpotDetailView.as_view(), name="spot_detail"),
    path("spots/neu/", views.SpotCreateView.as_view(), name="spot_create"),
    path("spots/<int:pk>/ändern/", views.SpotUpdateView.as_view(), name="spot_update"),
    path("spots/<int:pk>/löschen/", views.SpotDeleteView.as_view(), name="spot_delete"),
    path(
        "hinweis/neu/veranstaltung/",
        views.MessageEveCreateView.as_view(),
        name="message_eve_create",
    ),
    path(
        "hinweis/neu/trainingseinheit/",
        views.MessageSessCreateView.as_view(),
        name="message_sess_create",
    ),
    path(
        "hinweis/<int:pk>/löschen/",
        views.MessageDeleteView.as_view(),
        name="message_delete",
    ),
    path(
        "hinweis/<int:pk>/ändern/",
        views.MessageUpdateView.as_view(),
        name="message_update",
    ),
    path("gruppe/neu/", views.GroupCreateView.as_view(), name="group_create"),
    path(
        "gruppe/<int:pk>/ändern", views.GroupUpdateView.as_view(), name="group_update"
    ),
    path(
        "gruppe/<int:pk>/löschen/", views.GroupDeleteView.as_view(), name="group_delete"
    ),
    path(
        "gruppe/<int:pk>/detail/",
        views.RealGroupDetailView.as_view(),
        name="real_group_detail",
    ),
    path(
        "altersgruppe/neu/", views.AgeGroupCreateView.as_view(), name="agegroup_create"
    ),
    path(
        "altersgruppe/<int:pk>/ändern",
        views.AgeGroupUpdateView.as_view(),
        name="agegroup_update",
    ),
    path(
        "altersgruppe/<int:pk>/löschen/",
        views.AgeGroupDeleteView.as_view(),
        name="agegroup_delete",
    ),
    path(
        "altersgruppe/<int:pk>",
        views.AgeGroupDetailView.as_view(),
        name="agegroup_detail",
    ),
    path("profil/", views.UserDetailView.as_view(), name="profile_detail"),
    path(
        "profil/ändere_email/",
        views.EmailUpdateView.as_view(),
        name="profile_update_email",
    ),
    path(
        "profil/ändere_nutzername/",
        views.UsernameUpdateView.as_view(),
        name="profile_update_username",
    ),
    path(
        "profil/ändere_daten/",
        views.AddressChangeView.as_view(),
        name="profile_update_address",
    ),
    path(
        "profil/ändere_passwort/",
        views.PasswordChangeView.as_view(),
        name="profile_update_pw",
    ),
    path("beiträge/", views.NewsListView.as_view(), name="news_list"),
    path("beiträge/<int:pk>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("beiträge/neu/", views.NewsCreateView.as_view(), name="news_create"),
    path(
        "beiträge/<int:pk>/ändern", views.NewsUpdateView.as_view(), name="news_update"
    ),
    path(
        "beiträge/<int:pk>/löschen", views.NewsDeleteView.as_view(), name="news_delete"
    ),
    path("shop", views.ShopItemListView.as_view(), name="shop"),
    path(
        "shop/ändere_item/<int:pk>",
        views.ShopItemUpdateView.as_view(),
        name="shopitem_update",
    ),
    path("shop/neues_item/", views.create_shopitem, name="shopitem_create"),
    path(
        "shop/entferne_item/<int:pk>",
        views.ShopItemDeleteView.as_view(),
        name="shopitem_delete",
    ),
    path("ajax/get/bilder_daten", views.get_image_data, name="get_image_data"),
    path("ajax/set/bilder_daten", views.set_image_data, name="set_image_data"),
    path("ajax/entferne/bild", views.delete_image, name="delete_image"),
    path("ajax/hinzufügen/bild", views.add_image, name="upload_image_file"),
    path("ajax/weitere_email/neu", views.add_another_email, name="add_another_email"),
    path(
        "ajax/weitere_email/löschen",
        views.delete_additional_email,
        name="delete_additional_email",
    ),
    path(
        "ajax/weitere_email/löschen/<int:pk>",
        views.delete_additional_email_chair,
        name="delete_additional_email_chair",
    ),
]
