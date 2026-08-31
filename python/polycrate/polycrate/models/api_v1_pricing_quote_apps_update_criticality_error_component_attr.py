from typing import Literal

ApiV1PricingQuoteAppsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_QUOTE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_quote_apps_update_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
