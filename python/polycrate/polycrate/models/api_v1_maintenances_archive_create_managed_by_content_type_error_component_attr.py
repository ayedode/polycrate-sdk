from typing import Literal

ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_maintenances_archive_create_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
