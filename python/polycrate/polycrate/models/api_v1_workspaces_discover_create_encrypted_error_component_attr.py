from typing import Literal

ApiV1WorkspacesDiscoverCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_DISCOVER_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_discover_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
