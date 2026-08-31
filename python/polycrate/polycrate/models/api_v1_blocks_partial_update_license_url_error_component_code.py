from typing import Literal

ApiV1BlocksPartialUpdateLicenseUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_PARTIAL_UPDATE_LICENSE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateLicenseUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_partial_update_license_url_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateLicenseUrlErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_LICENSE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_LICENSE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
