from typing import Literal

ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponentAttr = Literal["additional_recipients"]

API_V1_MAINTENANCES_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponentAttr
] = {
    "additional_recipients",
}


def check_api_v1_maintenances_update_additional_recipients_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_ADDITIONAL_RECIPIENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
