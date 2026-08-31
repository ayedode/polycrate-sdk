from typing import Literal

ApiV1PricingQuotesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_quotes_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
