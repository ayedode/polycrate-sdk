from typing import Literal

ApiV1ProvidersReconcileCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_PROVIDERS_RECONCILE_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_providers_reconcile_create_emails_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateEmailsErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
