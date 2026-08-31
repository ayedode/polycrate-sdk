from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_encrypted_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEncryptedErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
