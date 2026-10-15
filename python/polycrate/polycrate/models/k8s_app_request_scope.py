from typing import Literal

K8SAppRequestScope = Literal["system", "user"]

K8S_APP_REQUEST_SCOPE_VALUES: set[K8SAppRequestScope] = {
    "system",
    "user",
}


def check_k8s_app_request_scope(value: str) -> K8SAppRequestScope:
    if value in K8S_APP_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_REQUEST_SCOPE_VALUES!r}")
