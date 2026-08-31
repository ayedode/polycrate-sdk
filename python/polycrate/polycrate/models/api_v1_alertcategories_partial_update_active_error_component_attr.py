from typing import Literal

ApiV1AlertcategoriesPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_alertcategories_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
