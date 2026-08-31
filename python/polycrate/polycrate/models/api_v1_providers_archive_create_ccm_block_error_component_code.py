from typing import Literal

ApiV1ProvidersArchiveCreateCcmBlockErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_ARCHIVE_CREATE_CCM_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateCcmBlockErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_archive_create_ccm_block_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateCcmBlockErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_CCM_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_CCM_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
