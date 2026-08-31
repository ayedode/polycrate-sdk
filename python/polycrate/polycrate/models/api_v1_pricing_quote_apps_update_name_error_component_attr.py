from typing import Literal

ApiV1PricingQuoteAppsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTE_APPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_quote_apps_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
