from typing import Literal

BlockListInstallationStatus = Literal["idle", "install_failed", "installing", "uninstall_failed", "uninstalling"]

BLOCK_LIST_INSTALLATION_STATUS_VALUES: set[BlockListInstallationStatus] = {
    "idle",
    "install_failed",
    "installing",
    "uninstall_failed",
    "uninstalling",
}


def check_block_list_installation_status(value: str) -> BlockListInstallationStatus:
    if value in BLOCK_LIST_INSTALLATION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_LIST_INSTALLATION_STATUS_VALUES!r}")
