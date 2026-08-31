from typing import Literal

ApiV1BlocksReconcileCreateTypeErrorComponentAttr = Literal["type"]

API_V1_BLOCKS_RECONCILE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateTypeErrorComponentAttr
] = {
    "type",
}


def check_api_v1_blocks_reconcile_create_type_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateTypeErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
