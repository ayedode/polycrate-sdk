from typing import Literal

ApiV1EndpointsReconcileCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_reconcile_create_archived_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateArchivedErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
