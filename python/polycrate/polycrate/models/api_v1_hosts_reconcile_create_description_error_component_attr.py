from typing import Literal

ApiV1HostsReconcileCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_HOSTS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_hosts_reconcile_create_description_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateDescriptionErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
