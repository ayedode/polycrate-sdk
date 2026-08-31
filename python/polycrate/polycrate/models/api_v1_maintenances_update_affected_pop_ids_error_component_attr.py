from typing import Literal

ApiV1MaintenancesUpdateAffectedPopIdsErrorComponentAttr = Literal["affected_pop_ids"]

API_V1_MAINTENANCES_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateAffectedPopIdsErrorComponentAttr
] = {
    "affected_pop_ids",
}


def check_api_v1_maintenances_update_affected_pop_ids_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateAffectedPopIdsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
