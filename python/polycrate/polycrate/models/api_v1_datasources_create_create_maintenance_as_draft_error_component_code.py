from typing import Literal

ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_CREATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_create_create_maintenance_as_draft_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
