from typing import Literal

ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_pricing_rules_archive_create_discount_type_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
