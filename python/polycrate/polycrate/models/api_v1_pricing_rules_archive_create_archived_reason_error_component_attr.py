from typing import Literal

ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_pricing_rules_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
