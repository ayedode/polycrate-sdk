from typing import Literal

ApiV1AlertcategoriesArchiveCreateActiveErrorComponentAttr = Literal["active"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_alertcategories_archive_create_active_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateActiveErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
