from typing import Literal

ApiV1MaintenancesPartialUpdateDraftErrorComponentAttr = Literal["draft"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateDraftErrorComponentAttr
] = {
    "draft",
}


def check_api_v1_maintenances_partial_update_draft_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateDraftErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
