from typing import Literal

K8SAppScope = Literal["system", "user"]

K8S_APP_SCOPE_VALUES: set[K8SAppScope] = {
    "system",
    "user",
}


def check_k8s_app_scope(value: str) -> K8SAppScope:
    if value in K8S_APP_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_SCOPE_VALUES!r}")
