from typing import Literal

ApiV1PricingQuotesArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_quotes_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
