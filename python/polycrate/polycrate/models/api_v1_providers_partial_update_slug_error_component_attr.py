from typing import Literal

ApiV1ProvidersPartialUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_PROVIDERS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_providers_partial_update_slug_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateSlugErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
