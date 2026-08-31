from typing import Literal

ApiV1AlertcategoriesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTCATEGORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertcategories_update_provider_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateProviderErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
