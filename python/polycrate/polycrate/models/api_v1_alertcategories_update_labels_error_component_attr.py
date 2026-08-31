from typing import Literal

ApiV1AlertcategoriesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTCATEGORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_alertcategories_update_labels_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesUpdateLabelsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
