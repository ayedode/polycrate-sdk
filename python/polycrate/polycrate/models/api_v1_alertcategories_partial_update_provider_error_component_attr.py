from typing import Literal

ApiV1AlertcategoriesPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertcategories_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
