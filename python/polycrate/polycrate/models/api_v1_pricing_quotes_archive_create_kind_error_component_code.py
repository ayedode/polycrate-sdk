from typing import Literal

ApiV1PricingQuotesArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quotes_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
