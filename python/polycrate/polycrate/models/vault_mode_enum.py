from typing import Literal

VaultModeEnum = Literal["dev", "ha", "standalone"]

VAULT_MODE_ENUM_VALUES: set[VaultModeEnum] = {
    "dev",
    "ha",
    "standalone",
}


def check_vault_mode_enum(value: str) -> VaultModeEnum:
    if value in VAULT_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VAULT_MODE_ENUM_VALUES!r}")
