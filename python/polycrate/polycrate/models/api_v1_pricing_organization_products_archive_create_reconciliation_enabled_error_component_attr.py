from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_pricing_organization_products_archive_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
