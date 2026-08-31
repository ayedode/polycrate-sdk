from typing import Literal

UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponentAttr = Literal["platform_dns_record_created"]

UI_K8S_APPS_INSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponentAttr
] = {
    "platform_dns_record_created",
}


def check_ui_k8s_apps_install_create_platform_dns_record_created_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreatePlatformDnsRecordCreatedErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
