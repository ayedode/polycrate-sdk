from typing import Literal

ApiV1WorkspacesDiscoverCreatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_DISCOVER_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_discover_create_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
