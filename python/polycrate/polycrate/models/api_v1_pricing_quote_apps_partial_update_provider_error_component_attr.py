from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quote_apps_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
