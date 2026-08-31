from typing import Literal

ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponentAttr = Literal["last_reconciliation_duration_seconds"]

API_V1_CVES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1_cves_create_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1CvesCreateLastReconciliationDurationSecondsErrorComponentAttr:
    if value in API_V1_CVES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
