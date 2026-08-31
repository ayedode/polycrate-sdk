from typing import Literal

ApiV1MaintenancesUpdateEndErrorComponentAttr = Literal["end"]

API_V1_MAINTENANCES_UPDATE_END_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesUpdateEndErrorComponentAttr] = {
    "end",
}


def check_api_v1_maintenances_update_end_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateEndErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
