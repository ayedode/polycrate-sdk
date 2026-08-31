from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_catalogue_apps_sync_releases_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
