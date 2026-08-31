from typing import Literal

ApiV1ContactsUpdateIsBillingContactErrorComponentCode = Literal["invalid", "null"]

API_V1_CONTACTS_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsUpdateIsBillingContactErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_contacts_update_is_billing_contact_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateIsBillingContactErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
