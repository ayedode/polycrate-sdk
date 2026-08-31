from typing import Literal

CategoryEnum = Literal[
    "application.customer",
    "availability.http",
    "backup.velero",
    "cluster.node",
    "data.cnpg",
    "data.mariadb",
    "data.mongodb",
    "data.replication",
    "gitops.flux",
    "observability.metrics",
    "platform.test",
    "security.access",
    "security.secrets",
    "storage.volume",
    "unknown",
    "workload.pod",
]

CATEGORY_ENUM_VALUES: set[CategoryEnum] = {
    "application.customer",
    "availability.http",
    "backup.velero",
    "cluster.node",
    "data.cnpg",
    "data.mariadb",
    "data.mongodb",
    "data.replication",
    "gitops.flux",
    "observability.metrics",
    "platform.test",
    "security.access",
    "security.secrets",
    "storage.volume",
    "unknown",
    "workload.pod",
}


def check_category_enum(value: str) -> CategoryEnum:
    if value in CATEGORY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATEGORY_ENUM_VALUES!r}")
