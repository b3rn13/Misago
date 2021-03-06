from django.utils.translation import gettext_lazy as _


class MisagoAdminExtension:
    def register_urlpatterns(self, urlpatterns):
        urlpatterns.namespace(r"^system/", "system")

    def register_navigation_nodes(self, site):
        site.add_node(
            name=_("System"),
            icon="fa fa-gears",
            parent="misago:admin",
            namespace="misago:admin:system",
            link="misago:admin:system:settings:index",
        )
