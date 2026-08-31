from typing import Literal

ApiV1WorkspacesCheckCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_CHECK_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_check_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
