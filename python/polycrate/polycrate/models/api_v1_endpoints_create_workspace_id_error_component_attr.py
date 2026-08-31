from typing import Literal

ApiV1EndpointsCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_ENDPOINTS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_endpoints_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
