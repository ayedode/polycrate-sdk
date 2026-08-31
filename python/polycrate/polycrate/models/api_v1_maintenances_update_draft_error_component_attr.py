from typing import Literal

ApiV1MaintenancesUpdateDraftErrorComponentAttr = Literal["draft"]

API_V1_MAINTENANCES_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesUpdateDraftErrorComponentAttr] = {
    "draft",
}


def check_api_v1_maintenances_update_draft_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateDraftErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
