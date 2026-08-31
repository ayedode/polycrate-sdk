from typing import Literal

InstallationStatusEnum = Literal["idle", "install_failed", "installing", "uninstall_failed", "uninstalling"]

INSTALLATION_STATUS_ENUM_VALUES: set[InstallationStatusEnum] = {
    "idle",
    "install_failed",
    "installing",
    "uninstall_failed",
    "uninstalling",
}


def check_installation_status_enum(value: str) -> InstallationStatusEnum:
    if value in INSTALLATION_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSTALLATION_STATUS_ENUM_VALUES!r}")
