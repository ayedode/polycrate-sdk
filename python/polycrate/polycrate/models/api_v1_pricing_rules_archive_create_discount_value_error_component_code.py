from typing import Literal

ApiV1PricingRulesArchiveCreateDiscountValueErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null", "required"
]

API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_VALUE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateDiscountValueErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
    "required",
}


def check_api_v1_pricing_rules_archive_create_discount_value_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateDiscountValueErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_VALUE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_VALUE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
