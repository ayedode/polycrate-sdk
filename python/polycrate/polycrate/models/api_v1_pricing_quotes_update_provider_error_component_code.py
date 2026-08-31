from typing import Literal

ApiV1PricingQuotesUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quotes_update_provider_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdateProviderErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
