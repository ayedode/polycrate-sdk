from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateSecretsEncryptionEnabledErrorComponentAttr = Literal[
    "secrets_encryption_enabled"
]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateSecretsEncryptionEnabledErrorComponentAttr
] = {
    "secrets_encryption_enabled",
}


def check_api_v1_kubernetes_controlplanes_archive_create_secrets_encryption_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateSecretsEncryptionEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
