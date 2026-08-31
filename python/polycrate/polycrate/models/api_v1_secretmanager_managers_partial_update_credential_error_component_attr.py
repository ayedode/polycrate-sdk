from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_secretmanager_managers_partial_update_credential_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
