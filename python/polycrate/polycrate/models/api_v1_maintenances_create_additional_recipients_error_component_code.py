from typing import Literal

ApiV1MaintenancesCreateAdditionalRecipientsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateAdditionalRecipientsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_create_additional_recipients_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateAdditionalRecipientsErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
