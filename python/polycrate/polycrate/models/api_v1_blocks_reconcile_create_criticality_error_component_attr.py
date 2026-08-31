from typing import Literal

ApiV1BlocksReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
