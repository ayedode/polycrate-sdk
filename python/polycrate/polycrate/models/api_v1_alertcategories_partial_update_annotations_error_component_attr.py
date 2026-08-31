from typing import Literal

ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertcategories_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
