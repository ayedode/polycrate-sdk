from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_catalogue_apps_sync_releases_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
