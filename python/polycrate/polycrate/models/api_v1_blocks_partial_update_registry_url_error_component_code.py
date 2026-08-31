from typing import Literal

ApiV1BlocksPartialUpdateRegistryUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateRegistryUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_partial_update_registry_url_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateRegistryUrlErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
