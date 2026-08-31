from typing import Literal

ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_alertcategories_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
