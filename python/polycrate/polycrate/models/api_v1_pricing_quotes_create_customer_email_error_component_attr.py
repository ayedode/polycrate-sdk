from typing import Literal

ApiV1PricingQuotesCreateCustomerEmailErrorComponentAttr = Literal["customer_email"]

API_V1_PRICING_QUOTES_CREATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateCustomerEmailErrorComponentAttr
] = {
    "customer_email",
}


def check_api_v1_pricing_quotes_create_customer_email_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateCustomerEmailErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
