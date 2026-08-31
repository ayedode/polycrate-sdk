from typing import Literal

ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_quotes_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
