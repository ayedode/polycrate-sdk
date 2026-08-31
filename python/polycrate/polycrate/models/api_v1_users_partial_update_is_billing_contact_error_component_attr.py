from typing import Literal

ApiV1UsersPartialUpdateIsBillingContactErrorComponentAttr = Literal["is_billing_contact"]

API_V1_USERS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1UsersPartialUpdateIsBillingContactErrorComponentAttr
] = {
    "is_billing_contact",
}


def check_api_v1_users_partial_update_is_billing_contact_error_component_attr(
    value: str,
) -> ApiV1UsersPartialUpdateIsBillingContactErrorComponentAttr:
    if value in API_V1_USERS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_PARTIAL_UPDATE_IS_BILLING_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
