from typing import Literal

ApiV1PricingRulesArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_rules_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateKindErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
