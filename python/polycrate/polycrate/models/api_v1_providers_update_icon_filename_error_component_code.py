from typing import Literal

ApiV1ProvidersUpdateIconFilenameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersUpdateIconFilenameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_update_icon_filename_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateIconFilenameErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
