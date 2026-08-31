from typing import Literal

ApiV1CredentialsReconcileCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_CREDENTIALS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_credentials_reconcile_create_description_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateDescriptionErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
