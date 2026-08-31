from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_maintenances_complete_early_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
