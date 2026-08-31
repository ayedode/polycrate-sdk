from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_pricing_organization_products_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
