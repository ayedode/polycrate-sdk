from typing import Literal

ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponentAttr = Literal["customer_name"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponentAttr
] = {
    "customer_name",
}


def check_api_v1_pricing_quotes_archive_create_customer_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_CUSTOMER_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
