from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_maintenances_complete_early_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
