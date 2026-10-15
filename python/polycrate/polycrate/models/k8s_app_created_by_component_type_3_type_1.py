from typing import Literal

K8SAppCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

K8S_APP_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[K8SAppCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_k8s_app_created_by_component_type_3_type_1(value: str) -> K8SAppCreatedByComponentType3Type1:
    if value in K8S_APP_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_APP_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
