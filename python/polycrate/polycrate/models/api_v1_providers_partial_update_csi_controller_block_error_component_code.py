from typing import Literal

ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_PARTIAL_UPDATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_partial_update_csi_controller_block_error_component_code(
    value: str,
) -> ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponentCode:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
