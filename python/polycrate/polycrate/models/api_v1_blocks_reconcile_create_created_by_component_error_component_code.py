from typing import Literal

ApiV1BlocksReconcileCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCKS_RECONCILE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_blocks_reconcile_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
