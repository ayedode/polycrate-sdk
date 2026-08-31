from typing import Literal

ApiV1KubernetesControlplanesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_kubernetes_controlplanes_list_organizations_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListOrganizationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
