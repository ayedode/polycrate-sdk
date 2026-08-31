from typing import Literal

ApiV1ContactsPartialUpdateIsBillingContactErrorComponentAttr = Literal["is_billing_contact"]

API_V1_CONTACTS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateIsBillingContactErrorComponentAttr
] = {
    "is_billing_contact",
}


def check_api_v1_contacts_partial_update_is_billing_contact_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateIsBillingContactErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
