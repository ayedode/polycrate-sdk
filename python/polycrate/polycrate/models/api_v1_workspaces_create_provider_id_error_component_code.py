from typing import Literal

ApiV1WorkspacesCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_create_provider_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateProviderIdErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
