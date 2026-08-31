from typing import Literal

ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_CHECK_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_check_create_secrets_poly_raw_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateSecretsPolyRawErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
