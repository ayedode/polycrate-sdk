from typing import Literal

ApiV1ProvidersIconUploadCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_icon_upload_create_active_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreateActiveErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
