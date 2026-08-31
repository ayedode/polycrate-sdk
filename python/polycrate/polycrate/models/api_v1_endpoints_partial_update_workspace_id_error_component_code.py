from typing import Literal

ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_endpoints_partial_update_workspace_id_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
