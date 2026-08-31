from typing import Literal

ApiV1BlocksCheckCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_CHECK_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_check_create_provider_id_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateProviderIdErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
