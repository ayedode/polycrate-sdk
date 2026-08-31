from typing import Literal

ApiV1AlertcategoriesCreateActiveErrorComponentAttr = Literal["active"]

API_V1_ALERTCATEGORIES_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_alertcategories_create_active_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateActiveErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
