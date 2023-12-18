from flask import Blueprint

from . import views

router = Blueprint(
    name="animations",
    import_name=__name__,
    url_prefix="/animations",
)

router.add_url_rule(
    rule="/",
    endpoint="index",
    view_func=views.index,
)

router.add_url_rule(
    rule="/circle",
    endpoint="circle",
    view_func=views.circle,
    methods=["GET", "POST"],
)
