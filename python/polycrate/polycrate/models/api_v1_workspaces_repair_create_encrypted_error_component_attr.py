from typing import Literal

ApiV1WorkspacesRepairCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_REPAIR_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_repair_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
