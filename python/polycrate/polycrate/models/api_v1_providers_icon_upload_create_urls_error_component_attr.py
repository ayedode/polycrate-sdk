from typing import Literal

ApiV1ProvidersIconUploadCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_providers_icon_upload_create_urls_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateUrlsErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
