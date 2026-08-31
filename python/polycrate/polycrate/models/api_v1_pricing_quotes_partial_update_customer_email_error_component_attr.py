from typing import Literal

ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponentAttr = Literal["customer_email"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponentAttr
] = {
    "customer_email",
}


def check_api_v1_pricing_quotes_partial_update_customer_email_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
