from typing import Literal

ApiV1WorkspacesUpdateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_update_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
