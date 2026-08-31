from typing import Literal

ApiV1KubernetesControlplanesListCreatedByUsersErrorComponentAttr = Literal["created_by_users"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListCreatedByUsersErrorComponentAttr
] = {
    "created_by_users",
}


def check_api_v1_kubernetes_controlplanes_list_created_by_users_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListCreatedByUsersErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
