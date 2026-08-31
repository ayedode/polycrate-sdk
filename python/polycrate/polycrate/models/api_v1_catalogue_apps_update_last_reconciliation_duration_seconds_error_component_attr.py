from typing import Literal

ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

API_V1_CATALOGUE_APPS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1_catalogue_apps_update_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
