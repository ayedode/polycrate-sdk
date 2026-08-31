from typing import Literal

ApiV1AlertcategoriesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTCATEGORIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertcategories_update_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
