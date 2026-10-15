from typing import Literal

AlertCategorySlug = Literal[
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

ALERT_CATEGORY_SLUG_VALUES: set[AlertCategorySlug] = {
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


def check_alert_category_slug(value: str) -> AlertCategorySlug:
    if value in ALERT_CATEGORY_SLUG_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_SLUG_VALUES!r}")
