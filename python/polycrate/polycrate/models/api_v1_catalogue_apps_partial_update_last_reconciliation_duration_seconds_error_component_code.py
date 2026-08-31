from typing import Literal

ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponentCode = Literal[
    "invalid", "max_string_length"
]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1_catalogue_apps_partial_update_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
