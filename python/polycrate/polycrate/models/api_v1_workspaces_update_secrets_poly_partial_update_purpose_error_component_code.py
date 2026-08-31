from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
