from typing import Literal

ApiV1BlocksUpdateRegistryUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_UPDATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateRegistryUrlErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_update_registry_url_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateRegistryUrlErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
