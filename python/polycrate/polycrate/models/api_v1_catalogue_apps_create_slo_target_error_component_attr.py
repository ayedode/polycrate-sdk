from typing import Literal

ApiV1CatalogueAppsCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_CATALOGUE_APPS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_catalogue_apps_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateSloTargetErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
