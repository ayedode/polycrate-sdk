from typing import Literal

ApiV1PricingQuotesArchiveCreateValidUntilErrorComponentAttr = Literal["valid_until"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateValidUntilErrorComponentAttr
] = {
    "valid_until",
}


def check_api_v1_pricing_quotes_archive_create_valid_until_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateValidUntilErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
