from typing import Literal

ApiV1WorkspacesDiscoverCreateEncryptedErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_DISCOVER_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreateEncryptedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_discover_create_encrypted_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateEncryptedErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
