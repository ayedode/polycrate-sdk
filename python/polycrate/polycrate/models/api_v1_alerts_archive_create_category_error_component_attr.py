from typing import Literal

ApiV1AlertsArchiveCreateCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_ARCHIVE_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateCategoryErrorComponentAttr
] = {
    "category",
}


def check_api_v1_alerts_archive_create_category_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
