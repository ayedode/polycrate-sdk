from typing import Literal

ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponentAttr = Literal["customer_email"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponentAttr
] = {
    "customer_email",
}


def check_api_v1_pricing_quotes_archive_create_customer_email_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_CUSTOMER_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
