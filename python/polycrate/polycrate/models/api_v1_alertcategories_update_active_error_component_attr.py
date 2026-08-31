from typing import Literal

ApiV1AlertcategoriesUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_ALERTCATEGORIES_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_alertcategories_update_active_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateActiveErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
