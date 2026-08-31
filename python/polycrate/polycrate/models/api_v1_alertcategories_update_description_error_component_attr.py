from typing import Literal

ApiV1AlertcategoriesUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_ALERTCATEGORIES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_alertcategories_update_description_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateDescriptionErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
