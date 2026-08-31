from typing import Literal

ApiV1BlocksReconcileCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_reconcile_create_archived_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateArchivedErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
