from typing import Literal

ApiV1BlocksLogsReloadCreateAppVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateAppVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_logs_reload_create_app_version_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateAppVersionErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
