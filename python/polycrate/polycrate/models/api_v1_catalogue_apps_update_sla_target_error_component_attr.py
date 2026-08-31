from typing import Literal

ApiV1CatalogueAppsUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_CATALOGUE_APPS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_catalogue_apps_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
