from typing import Literal

ApiV1MaintenancesPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_maintenances_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
