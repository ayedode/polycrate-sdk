from typing import Literal

ApiV1PricingRulesArchiveCreateProductKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateProductKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_rules_archive_create_product_kind_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateProductKindErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_PRODUCT_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
