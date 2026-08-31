from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_quote_apps_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
