from typing import Literal

ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_ARCHIVE_CREATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_archive_create_csi_controller_block_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
