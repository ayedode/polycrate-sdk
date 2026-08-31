from typing import Literal

ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_quotes_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
