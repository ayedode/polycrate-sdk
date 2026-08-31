from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_quote_apps_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
