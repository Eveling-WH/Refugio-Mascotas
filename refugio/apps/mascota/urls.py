from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete,vacuna_view, vacuna_list, vacuna_edit, vacuna_delete, MascotaList,\
MascotaCreate, MascotaUpdate, MascotaDelete, VacunaList, VacunaCreate, VacunaUpdate, VacunaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),

    url(r'^vacuna/listar$', vacuna_list, name='vacuna_listar'),
    url(r'^vacuna$', vacuna_view, name='vacuna_crear'),
    url(r'^vacuna/editar/(?P<id_vacuna>\d+)/$', vacuna_edit, name='vacuna_editar'),
    url(r'^vacuna/eliminar/(?P<id_vacuna>\d+)/$', vacuna_delete, name='vacuna_eliminar'),

    url(r'^clases/listar$', MascotaList.as_view(), name='mascota_listar_clases'),
    url(r'^clases/nuevo$', MascotaCreate.as_view(), name='mascota_crear_clases'),
    url(r'^clases/editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar_clases'),
    url(r'^clases/eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar_clases'),

    url(r'^clases/vacuna/listar$', VacunaList.as_view(), name='vacuna_listar_clases'),
    url(r'^clases/vacuna/nuevo$', VacunaCreate.as_view(), name='vacuna_crear_clases'),
    url(r'^clases/vacuna/editar/(?P<pk>\d+)/$', VacunaUpdate.as_view(), name='vacuna_editar_clases'),
    url(r'^clases/vacuna/eliminar/(?P<pk>\d+)/$', VacunaDelete.as_view(), name='vacuna_eliminar_clases'),

]
 