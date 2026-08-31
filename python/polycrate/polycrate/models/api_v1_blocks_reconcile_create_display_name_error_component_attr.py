from typing import Literal

ApiV1BlocksReconcileCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_BLOCKS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_blocks_reconcile_create_display_name_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateDisplayNameErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
