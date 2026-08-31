from typing import Literal

ApiV1BlocksReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCKS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_blocks_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateNameErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
