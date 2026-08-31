from typing import Literal

ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_partial_update_is_billing_contact_error_component_code(
    value: str,
) -> ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponentCode:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
