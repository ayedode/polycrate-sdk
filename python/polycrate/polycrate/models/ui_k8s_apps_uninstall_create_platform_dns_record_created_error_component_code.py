from typing import Literal

UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_uninstall_create_platform_dns_record_created_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
