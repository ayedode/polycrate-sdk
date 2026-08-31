from typing import Literal

ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_ENDPOINTS_DISCOVER_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_endpoints_discover_create_workspace_id_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
