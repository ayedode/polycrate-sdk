from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponentAttr = Literal["additional_recipients"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponentAttr
] = {
    "additional_recipients",
}


def check_api_v1_maintenances_complete_early_create_additional_recipients_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
