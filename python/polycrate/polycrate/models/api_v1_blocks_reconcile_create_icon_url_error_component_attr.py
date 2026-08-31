from typing import Literal

ApiV1BlocksReconcileCreateIconUrlErrorComponentAttr = Literal["icon_url"]

API_V1_BLOCKS_RECONCILE_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateIconUrlErrorComponentAttr
] = {
    "icon_url",
}


def check_api_v1_blocks_reconcile_create_icon_url_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateIconUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
