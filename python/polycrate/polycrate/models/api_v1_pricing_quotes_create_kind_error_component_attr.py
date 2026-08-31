from typing import Literal

ApiV1PricingQuotesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingQuotesCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pricing_quotes_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
