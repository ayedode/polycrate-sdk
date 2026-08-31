from typing import Literal

ApiV1CatalogueAppsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_CATALOGUE_APPS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_catalogue_apps_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
