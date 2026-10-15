from typing import Literal

PatchedSecretManagerRequestVaultModeType1 = Literal["", "dev", "ha", "standalone"]

PATCHED_SECRET_MANAGER_REQUEST_VAULT_MODE_TYPE_1_VALUES: set[PatchedSecretManagerRequestVaultModeType1] = {
    "",
    "dev",
    "ha",
    "standalone",
}


def check_patched_secret_manager_request_vault_mode_type_1(value: str) -> PatchedSecretManagerRequestVaultModeType1:
    if value in PATCHED_SECRET_MANAGER_REQUEST_VAULT_MODE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_SECRET_MANAGER_REQUEST_VAULT_MODE_TYPE_1_VALUES!r}"
    )
