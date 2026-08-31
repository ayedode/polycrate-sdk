from typing import Literal

ApiV1ProvidersIconUploadCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_providers_icon_upload_create_provider_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreateProviderErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
