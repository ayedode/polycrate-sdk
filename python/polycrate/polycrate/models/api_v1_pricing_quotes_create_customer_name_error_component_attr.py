from typing import Literal

ApiV1PricingQuotesCreateCustomerNameErrorComponentAttr = Literal["customer_name"]

API_V1_PRICING_QUOTES_CREATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateCustomerNameErrorComponentAttr
] = {
    "customer_name",
}


def check_api_v1_pricing_quotes_create_customer_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateCustomerNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
