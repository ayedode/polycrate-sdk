from typing import Literal

ApiV1PricingQuoteAppsUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_QUOTE_APPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_quote_apps_update_name_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateNameErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
