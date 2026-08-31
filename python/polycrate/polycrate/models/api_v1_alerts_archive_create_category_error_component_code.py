from typing import Literal

ApiV1AlertsArchiveCreateCategoryErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTS_ARCHIVE_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsArchiveCreateCategoryErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alerts_archive_create_category_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateCategoryErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
