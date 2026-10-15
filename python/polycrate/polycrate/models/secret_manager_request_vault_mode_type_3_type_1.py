from typing import Literal

SecretManagerRequestVaultModeType3Type1 = Literal["", "dev", "ha", "standalone"]

SECRET_MANAGER_REQUEST_VAULT_MODE_TYPE_3_TYPE_1_VALUES: set[SecretManagerRequestVaultModeType3Type1] = {
    "",
    "dev",
    "ha",
    "standalone",
}


def check_secret_manager_request_vault_mode_type_3_type_1(value: str) -> SecretManagerRequestVaultModeType3Type1:
    if value in SECRET_MANAGER_REQUEST_VAULT_MODE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_REQUEST_VAULT_MODE_TYPE_3_TYPE_1_VALUES!r}"
    )
