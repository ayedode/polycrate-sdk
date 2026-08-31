from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_apps_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
