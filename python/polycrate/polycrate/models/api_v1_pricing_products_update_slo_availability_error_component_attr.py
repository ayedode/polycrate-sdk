from typing import Literal

ApiV1PricingProductsUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PRICING_PRODUCTS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_pricing_products_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1PricingProductsUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
