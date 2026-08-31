from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateKindErrorComponentAttr = Literal["kind"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_maintenances_complete_early_create_kind_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateKindErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
