from typing import Literal

ApiV1PricingQuotesUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_pricing_quotes_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
