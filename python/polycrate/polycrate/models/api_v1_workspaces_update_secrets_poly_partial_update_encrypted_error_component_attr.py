from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
