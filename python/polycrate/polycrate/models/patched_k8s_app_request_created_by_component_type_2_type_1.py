from typing import Literal

PatchedK8SAppRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

PATCHED_K8S_APP_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    PatchedK8SAppRequestCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_k8s_app_request_created_by_component_type_2_type_1(
    value: str,
) -> PatchedK8SAppRequestCreatedByComponentType2Type1:
    if value in PATCHED_K8S_APP_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_APP_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
