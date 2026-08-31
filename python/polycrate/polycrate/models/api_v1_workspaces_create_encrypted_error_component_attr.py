from typing import Literal

ApiV1WorkspacesCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
