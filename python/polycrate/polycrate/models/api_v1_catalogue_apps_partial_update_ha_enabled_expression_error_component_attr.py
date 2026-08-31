from typing import Literal

ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponentAttr = Literal["ha_enabled_expression"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_HA_ENABLED_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponentAttr
] = {
    "ha_enabled_expression",
}


def check_api_v1_catalogue_apps_partial_update_ha_enabled_expression_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_HA_ENABLED_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_HA_ENABLED_EXPRESSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
