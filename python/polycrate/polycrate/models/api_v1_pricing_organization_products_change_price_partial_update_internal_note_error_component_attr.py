from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponentAttr = Literal["internal_note"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_INTERNAL_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponentAttr
] = {
    "internal_note",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_internal_note_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponentAttr:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_INTERNAL_NOTE_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_INTERNAL_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
