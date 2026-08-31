from typing import Literal

ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_alertcategories_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
