from typing import Literal

ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_rules_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
