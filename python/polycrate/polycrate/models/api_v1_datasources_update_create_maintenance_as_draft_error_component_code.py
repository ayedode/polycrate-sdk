from typing import Literal

ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_UPDATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_update_create_maintenance_as_draft_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_CREATE_MAINTENANCE_AS_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
