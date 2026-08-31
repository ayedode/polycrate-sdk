from typing import Literal

ApiV1AlertcategoriesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTCATEGORIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_alertcategories_create_labels_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateLabelsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
