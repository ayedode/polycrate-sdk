from typing import Literal

ApiV1AlertcategoriesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_alertcategories_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
