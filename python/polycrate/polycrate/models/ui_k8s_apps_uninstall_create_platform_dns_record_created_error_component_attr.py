from typing import Literal

UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponentAttr = Literal["platform_dns_record_created"]

UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponentAttr
] = {
    "platform_dns_record_created",
}


def check_ui_k8s_apps_uninstall_create_platform_dns_record_created_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePlatformDnsRecordCreatedErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
