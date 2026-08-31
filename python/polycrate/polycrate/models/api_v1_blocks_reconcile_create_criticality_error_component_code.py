from typing import Literal

ApiV1BlocksReconcileCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCKS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_blocks_reconcile_create_criticality_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateCriticalityErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
