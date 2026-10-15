from typing import Literal

K8SAppCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

K8S_APP_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[K8SAppCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_k8s_app_created_by_component_type_2_type_1(value: str) -> K8SAppCreatedByComponentType2Type1:
    if value in K8S_APP_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_APP_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
