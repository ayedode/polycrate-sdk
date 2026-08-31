from typing import Literal

ApiV1PricingQuoteAppsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTE_APPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quote_apps_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
