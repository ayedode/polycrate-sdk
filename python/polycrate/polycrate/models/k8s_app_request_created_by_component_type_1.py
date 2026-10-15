from typing import Literal

K8SAppRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

K8S_APP_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[K8SAppRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_k8s_app_request_created_by_component_type_1(value: str) -> K8SAppRequestCreatedByComponentType1:
    if value in K8S_APP_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_APP_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
