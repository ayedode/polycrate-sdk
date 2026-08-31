from typing import Literal

ApiV1PricingQuotesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quotes_update_archived_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdateArchivedErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
