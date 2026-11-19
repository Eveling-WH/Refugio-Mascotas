from django.conf.urls import url
from apps.adopcion.views import index_adopcion, adoptante_list, adoptante_edit, adoptante_delete, adoptante_view,\
AdoptanteList, AdoptanteCreate, AdoptamteUpdate,AdoptanteDelete, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete,\
solicitud_list, solicitud_view, solicitud_delete, solicitud_edit

urlpatterns = [
    url(r'^index$', index_adopcion),
    url(r'^nuevo$', adoptante_view, name='adoptante_crear'),
    url(r'^listars$', adoptante_list, name='adoptante_listar'),
    url(r'^editar/(?P<id_persona>\d+)/$', adoptante_edit, name='adoptante_editar'),
    url(r'^eliminar/(?P<id_persona>\d+)/$', adoptante_delete, name='adoptante_eliminar'),

    url(r'^clases/listars$', AdoptanteList.as_view(), name='adoptante_listar_clases'),
    url(r'^clases/nuevo$', AdoptanteCreate.as_view(), name='adoptante_crear_clases'),
    url(r'^clases/editar/(?P<pk>\d+)/$', AdoptamteUpdate.as_view(), name='adoptante_editar_clases'),
    url(r'^clases/eliminar/(?P<pk>\d+)/$', AdoptanteDelete.as_view(), name='adoptante_eliminar_clases'),

    url(r'^clases/solicitud$', SolicitudList.as_view(), name='solicitud_listar_clases'),
    url(r'^clases/solicitud/crear$', SolicitudCreate.as_view(), name='solicitud_crear_clases'),
    url(r'^clases/solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar_clases'),
    url(r'^clases/solicitud/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_eliminar_clases'),

    url(r'^listars/solicitud$', solicitud_list, name='solicitud_listar'),
    url(r'^nuevo/solicitud$', solicitud_view, name='solicitud_crear'),
    url(r'^eliminar/solicitud/(?P<id_solicitud>\d+)/$', solicitud_delete, name='solicitud_eliminar'),
    url(r'^editar/solicitud/(?P<id_solicitud>\d+)/$', solicitud_edit, name='solicitud_editar'),
]
 
