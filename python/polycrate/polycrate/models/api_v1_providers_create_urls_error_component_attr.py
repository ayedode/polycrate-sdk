from typing import Literal

ApiV1ProvidersCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROVIDERS_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersCreateUrlsErrorComponentAttr] = {
    "urls",
}


def check_api_v1_providers_create_urls_error_component_attr(value: str) -> ApiV1ProvidersCreateUrlsErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
