from typing import Literal

ApiV1AlertcategoriesCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alertcategories_create_archived_at_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesCreateArchivedAtErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
