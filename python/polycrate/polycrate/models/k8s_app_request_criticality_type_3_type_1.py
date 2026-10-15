from typing import Literal

K8SAppRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

K8S_APP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[K8SAppRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_k8s_app_request_criticality_type_3_type_1(value: str) -> K8SAppRequestCriticalityType3Type1:
    if value in K8S_APP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
