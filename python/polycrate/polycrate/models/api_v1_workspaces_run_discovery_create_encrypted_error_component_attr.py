from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_run_discovery_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
