from typing import Literal

ApiV1ProvidersPartialUpdateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROVIDERS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_providers_partial_update_urls_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateUrlsErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
