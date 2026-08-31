from typing import Literal

ApiV1PricingQuotesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quotes_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
