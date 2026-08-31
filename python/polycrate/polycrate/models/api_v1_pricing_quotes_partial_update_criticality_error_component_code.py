from typing import Literal

ApiV1PricingQuotesPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_quotes_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
