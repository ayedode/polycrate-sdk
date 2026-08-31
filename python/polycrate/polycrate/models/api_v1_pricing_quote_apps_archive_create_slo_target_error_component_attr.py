from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_quote_apps_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
