from typing import Literal

ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponentAttr = Literal["secrets_encryption_enabled"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponentAttr
] = {
    "secrets_encryption_enabled",
}


def check_api_v1_kubernetes_controlplanes_create_secrets_encryption_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
