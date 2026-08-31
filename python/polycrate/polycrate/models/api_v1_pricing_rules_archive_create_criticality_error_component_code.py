from typing import Literal

ApiV1PricingRulesArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_rules_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
