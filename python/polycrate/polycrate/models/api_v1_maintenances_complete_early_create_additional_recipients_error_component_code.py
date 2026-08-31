from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_complete_early_create_additional_recipients_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
