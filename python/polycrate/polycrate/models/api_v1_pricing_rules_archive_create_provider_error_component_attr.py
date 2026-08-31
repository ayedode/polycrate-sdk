from typing import Literal

ApiV1PricingRulesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_rules_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
