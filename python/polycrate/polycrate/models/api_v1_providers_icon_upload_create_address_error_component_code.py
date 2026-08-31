from typing import Literal

ApiV1ProvidersIconUploadCreateAddressErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreateAddressErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_icon_upload_create_address_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreateAddressErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
