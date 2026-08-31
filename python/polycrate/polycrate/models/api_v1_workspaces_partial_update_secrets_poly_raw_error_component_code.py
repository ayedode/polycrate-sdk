from typing import Literal

ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_PARTIAL_UPDATE_SECRETS_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_partial_update_secrets_poly_raw_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateSecretsPolyRawErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_SECRETS_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_SECRETS_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
