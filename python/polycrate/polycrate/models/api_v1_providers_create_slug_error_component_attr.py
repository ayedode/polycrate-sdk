from typing import Literal

ApiV1ProvidersCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_PROVIDERS_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersCreateSlugErrorComponentAttr] = {
    "slug",
}


def check_api_v1_providers_create_slug_error_component_attr(value: str) -> ApiV1ProvidersCreateSlugErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
