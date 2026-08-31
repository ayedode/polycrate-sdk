from typing import Literal

ApiV1MaintenancesUpdateDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1MaintenancesUpdateDraftErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_update_draft_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateDraftErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
