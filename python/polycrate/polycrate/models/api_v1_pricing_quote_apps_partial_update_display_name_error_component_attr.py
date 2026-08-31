from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_quote_apps_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
