from typing import Literal

ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_logs_reload_create_registry_url_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateRegistryUrlErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
