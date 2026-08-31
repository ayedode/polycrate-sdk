from typing import Literal

ApiV1SecretmanagerManagersCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_secretmanager_managers_create_credential_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateCredentialErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
