from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponentAttr = Literal["affected_pop_ids"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponentAttr
] = {
    "affected_pop_ids",
}


def check_api_v1_maintenances_complete_early_create_affected_pop_ids_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
