from typing import Literal

ApiV1PricingQuotesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quotes_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
