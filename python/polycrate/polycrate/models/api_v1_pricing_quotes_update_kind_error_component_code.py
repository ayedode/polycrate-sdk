from typing import Literal

ApiV1PricingQuotesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PricingQuotesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quotes_update_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdateKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
