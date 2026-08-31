from typing import Literal

ApiV1ContactsCreateIsBillingContactErrorComponentCode = Literal["invalid", "null"]

API_V1_CONTACTS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsCreateIsBillingContactErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_contacts_create_is_billing_contact_error_component_code(
    value: str,
) -> ApiV1ContactsCreateIsBillingContactErrorComponentCode:
    if value in API_V1_CONTACTS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
