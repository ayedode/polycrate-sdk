from typing import Literal

ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_run_discovery_create_icon_url_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateIconUrlErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
