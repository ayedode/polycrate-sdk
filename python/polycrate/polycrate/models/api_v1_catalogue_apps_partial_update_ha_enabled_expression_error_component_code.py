from typing import Literal

ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_HA_ENABLED_EXPRESSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_partial_update_ha_enabled_expression_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_HA_ENABLED_EXPRESSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_HA_ENABLED_EXPRESSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
