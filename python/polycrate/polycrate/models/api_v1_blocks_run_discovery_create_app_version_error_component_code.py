from typing import Literal

ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_run_discovery_create_app_version_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateAppVersionErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
