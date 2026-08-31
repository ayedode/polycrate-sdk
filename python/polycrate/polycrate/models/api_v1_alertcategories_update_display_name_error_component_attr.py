from typing import Literal

ApiV1AlertcategoriesUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ALERTCATEGORIES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_alertcategories_update_display_name_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
