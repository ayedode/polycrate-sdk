from typing import Literal

ApiV1AlertcategoriesCreateNameErrorComponentAttr = Literal["name"]

API_V1_ALERTCATEGORIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_alertcategories_create_name_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateNameErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
