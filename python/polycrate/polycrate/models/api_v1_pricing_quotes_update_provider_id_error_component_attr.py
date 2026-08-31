from typing import Literal

ApiV1PricingQuotesUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_pricing_quotes_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateProviderIdErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
