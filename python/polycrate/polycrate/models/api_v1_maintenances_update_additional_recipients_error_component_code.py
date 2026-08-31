from typing import Literal

ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_update_additional_recipients_error_component_code(
    value: str,
) -> ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponentCode:
    if value in API_V1_MAINTENANCES_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
