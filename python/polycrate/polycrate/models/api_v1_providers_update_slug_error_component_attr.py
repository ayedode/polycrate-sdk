from typing import Literal

ApiV1ProvidersUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_PROVIDERS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateSlugErrorComponentAttr] = {
    "slug",
}


def check_api_v1_providers_update_slug_error_component_attr(value: str) -> ApiV1ProvidersUpdateSlugErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
