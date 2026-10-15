from typing import Literal

SecretManagerVaultModeType1 = Literal["", "dev", "ha", "standalone"]

SECRET_MANAGER_VAULT_MODE_TYPE_1_VALUES: set[SecretManagerVaultModeType1] = {
    "",
    "dev",
    "ha",
    "standalone",
}


def check_secret_manager_vault_mode_type_1(value: str) -> SecretManagerVaultModeType1:
    if value in SECRET_MANAGER_VAULT_MODE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_VAULT_MODE_TYPE_1_VALUES!r}")
