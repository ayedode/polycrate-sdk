from typing import Literal

ApiV1AdminUsersCreateIsBillingContactErrorComponentAttr = Literal["is_billing_contact"]

API_V1_ADMIN_USERS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersCreateIsBillingContactErrorComponentAttr
] = {
    "is_billing_contact",
}


def check_api_v1_admin_users_create_is_billing_contact_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateIsBillingContactErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
