from typing import Literal

BlockInstallationStatus = Literal["idle", "install_failed", "installing", "uninstall_failed", "uninstalling"]

BLOCK_INSTALLATION_STATUS_VALUES: set[BlockInstallationStatus] = {
    "idle",
    "install_failed",
    "installing",
    "uninstall_failed",
    "uninstalling",
}


def check_block_installation_status(value: str) -> BlockInstallationStatus:
    if value in BLOCK_INSTALLATION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_INSTALLATION_STATUS_VALUES!r}")
