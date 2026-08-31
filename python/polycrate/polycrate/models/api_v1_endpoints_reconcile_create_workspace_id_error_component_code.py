from typing import Literal

ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_ENDPOINTS_RECONCILE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_endpoints_reconcile_create_workspace_id_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
