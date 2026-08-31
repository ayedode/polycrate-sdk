from typing import Literal

ApiV1ProvidersIconUploadCreatePhoneErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PHONE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreatePhoneErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_icon_upload_create_phone_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreatePhoneErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PHONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PHONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
