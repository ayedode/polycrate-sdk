from typing import Literal

ApiV1AlertcategoriesCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertcategories_create_archived_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesCreateArchivedErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
