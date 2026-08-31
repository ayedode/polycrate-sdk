from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_maintenances_complete_early_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
