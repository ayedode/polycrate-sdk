from typing import Literal

ApiV1AlertcategoriesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
