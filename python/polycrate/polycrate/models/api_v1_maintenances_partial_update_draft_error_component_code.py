from typing import Literal

ApiV1MaintenancesPartialUpdateDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateDraftErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_partial_update_draft_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateDraftErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
