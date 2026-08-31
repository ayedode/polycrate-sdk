from typing import Literal

ApiV1PricingQuotesArchiveCreateValidUntilErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_VALID_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesArchiveCreateValidUntilErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_quotes_archive_create_valid_until_error_component_code(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateValidUntilErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_VALID_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_VALID_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
