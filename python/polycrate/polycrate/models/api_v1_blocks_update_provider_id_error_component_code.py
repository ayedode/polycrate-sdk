from typing import Literal

ApiV1BlocksUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateProviderIdErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_update_provider_id_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateProviderIdErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
