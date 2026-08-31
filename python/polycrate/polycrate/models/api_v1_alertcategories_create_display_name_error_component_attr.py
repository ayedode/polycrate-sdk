from typing import Literal

ApiV1AlertcategoriesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ALERTCATEGORIES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_alertcategories_create_display_name_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
