from typing import Literal

ApiV1PricingRulesArchiveCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_RULES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_rules_archive_create_sla_target_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateSlaTargetErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
