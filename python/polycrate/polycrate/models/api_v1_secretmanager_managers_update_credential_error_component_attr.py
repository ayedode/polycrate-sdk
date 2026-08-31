from typing import Literal

ApiV1SecretmanagerManagersUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_secretmanager_managers_update_credential_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateCredentialErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
