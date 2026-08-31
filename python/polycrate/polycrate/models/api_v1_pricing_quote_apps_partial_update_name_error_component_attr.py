from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_quote_apps_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
