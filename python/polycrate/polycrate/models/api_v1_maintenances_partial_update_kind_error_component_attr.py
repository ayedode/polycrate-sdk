from typing import Literal

ApiV1MaintenancesPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_maintenances_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateKindErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
