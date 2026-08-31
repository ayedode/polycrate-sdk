from typing import Literal

ApiV1PricingQuotesPartialUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesPartialUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_quotes_partial_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
