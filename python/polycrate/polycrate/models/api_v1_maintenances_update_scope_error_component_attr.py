from typing import Literal

ApiV1MaintenancesUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_MAINTENANCES_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_maintenances_update_scope_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateScopeErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
