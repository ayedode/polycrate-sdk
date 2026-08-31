from typing import Literal

ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponentAttr = Literal["customer_name"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponentAttr
] = {
    "customer_name",
}


def check_api_v1_pricing_quotes_partial_update_customer_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
