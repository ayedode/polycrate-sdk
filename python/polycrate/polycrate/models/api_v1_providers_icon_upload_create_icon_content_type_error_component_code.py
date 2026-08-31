from typing import Literal

ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_icon_upload_create_icon_content_type_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
