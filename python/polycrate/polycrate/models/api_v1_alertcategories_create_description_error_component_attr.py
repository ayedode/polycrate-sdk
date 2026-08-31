from typing import Literal

ApiV1AlertcategoriesCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_ALERTCATEGORIES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_alertcategories_create_description_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateDescriptionErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
