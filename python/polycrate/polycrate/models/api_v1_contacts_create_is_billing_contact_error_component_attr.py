from typing import Literal

ApiV1ContactsCreateIsBillingContactErrorComponentAttr = Literal["is_billing_contact"]

API_V1_CONTACTS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsCreateIsBillingContactErrorComponentAttr
] = {
    "is_billing_contact",
}


def check_api_v1_contacts_create_is_billing_contact_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateIsBillingContactErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
