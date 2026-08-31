from typing import Literal

ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_organization_products_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
