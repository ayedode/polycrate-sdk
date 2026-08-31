from typing import Literal

ApiV1AlertcategoriesCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ALERTCATEGORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_alertcategories_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateProviderIdErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
