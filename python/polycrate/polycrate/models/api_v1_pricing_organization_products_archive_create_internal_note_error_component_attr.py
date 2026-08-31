from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponentAttr = Literal["internal_note"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_INTERNAL_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponentAttr
] = {
    "internal_note",
}


def check_api_v1_pricing_organization_products_archive_create_internal_note_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_INTERNAL_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_INTERNAL_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
