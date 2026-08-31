from typing import Literal

ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponentAttr = Literal["create_maintenance_as_draft"]

API_V1_DATASOURCES_ARCHIVE_CREATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponentAttr
] = {
    "create_maintenance_as_draft",
}


def check_api_v1_datasources_archive_create_create_maintenance_as_draft_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
