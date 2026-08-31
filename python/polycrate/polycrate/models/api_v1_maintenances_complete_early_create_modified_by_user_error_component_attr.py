from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_maintenances_complete_early_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
