from typing import Literal

ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_logs_reload_create_alternative_name_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateAlternativeNameErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
