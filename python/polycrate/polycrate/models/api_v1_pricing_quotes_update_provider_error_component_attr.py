from typing import Literal

ApiV1PricingQuotesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quotes_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
