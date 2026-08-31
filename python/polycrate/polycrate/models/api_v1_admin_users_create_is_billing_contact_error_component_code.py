from typing import Literal

ApiV1AdminUsersCreateIsBillingContactErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersCreateIsBillingContactErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_create_is_billing_contact_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateIsBillingContactErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
