from typing import Literal

ApiV1ContactsUpdateIsBillingContactErrorComponentAttr = Literal["is_billing_contact"]

API_V1_CONTACTS_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsUpdateIsBillingContactErrorComponentAttr
] = {
    "is_billing_contact",
}


def check_api_v1_contacts_update_is_billing_contact_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateIsBillingContactErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
