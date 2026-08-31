from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSystemConfigUpdateRequestRequest")


@_attrs_define
class PatchedSystemConfigUpdateRequestRequest:
    """
    Attributes:
        system_owner_organization (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        system_host_cluster (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        system_apm_cluster (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_support_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_s3_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_assistant_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_loadbalancer_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_k8s_volume_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_internal_dns_zone_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_external_dns_zone_product (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        system_domain_registrar (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_s3_bucket_cluster (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        system_default_pop (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        k8s_cluster_backup_s3_cluster (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        default_k8s_cluster_dns_zone (str | Unset): Primary key UUID string, or blank to clear the foreign key.
        system_name (str | Unset):
        system_frontend_base_url (str | Unset):
        platform_dns_zone (str | Unset):
        global_debug_mode (bool | Unset):
        system_reconciliation_interval_seconds (int | Unset):
        system_discovery_interval_seconds (int | Unset):
        discovery_enabled (bool | Unset):
        reconciliation_enabled (bool | Unset):
    """

    system_owner_organization: str | Unset = UNSET
    system_host_cluster: str | Unset = UNSET
    system_apm_cluster: str | Unset = UNSET
    default_support_product: str | Unset = UNSET
    default_s3_product: str | Unset = UNSET
    default_assistant_product: str | Unset = UNSET
    default_loadbalancer_product: str | Unset = UNSET
    default_k8s_volume_product: str | Unset = UNSET
    default_internal_dns_zone_product: str | Unset = UNSET
    default_external_dns_zone_product: str | Unset = UNSET
    system_domain_registrar: str | Unset = UNSET
    default_s3_bucket_cluster: str | Unset = UNSET
    system_default_pop: str | Unset = UNSET
    k8s_cluster_backup_s3_cluster: str | Unset = UNSET
    default_k8s_cluster_dns_zone: str | Unset = UNSET
    system_name: str | Unset = UNSET
    system_frontend_base_url: str | Unset = UNSET
    platform_dns_zone: str | Unset = UNSET
    global_debug_mode: bool | Unset = UNSET
    system_reconciliation_interval_seconds: int | Unset = UNSET
    system_discovery_interval_seconds: int | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_owner_organization = self.system_owner_organization

        system_host_cluster = self.system_host_cluster

        system_apm_cluster = self.system_apm_cluster

        default_support_product = self.default_support_product

        default_s3_product = self.default_s3_product

        default_assistant_product = self.default_assistant_product

        default_loadbalancer_product = self.default_loadbalancer_product

        default_k8s_volume_product = self.default_k8s_volume_product

        default_internal_dns_zone_product = self.default_internal_dns_zone_product

        default_external_dns_zone_product = self.default_external_dns_zone_product

        system_domain_registrar = self.system_domain_registrar

        default_s3_bucket_cluster = self.default_s3_bucket_cluster

        system_default_pop = self.system_default_pop

        k8s_cluster_backup_s3_cluster = self.k8s_cluster_backup_s3_cluster

        default_k8s_cluster_dns_zone = self.default_k8s_cluster_dns_zone

        system_name = self.system_name

        system_frontend_base_url = self.system_frontend_base_url

        platform_dns_zone = self.platform_dns_zone

        global_debug_mode = self.global_debug_mode

        system_reconciliation_interval_seconds = self.system_reconciliation_interval_seconds

        system_discovery_interval_seconds = self.system_discovery_interval_seconds

        discovery_enabled = self.discovery_enabled

        reconciliation_enabled = self.reconciliation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system_owner_organization is not UNSET:
            field_dict["system_owner_organization"] = system_owner_organization
        if system_host_cluster is not UNSET:
            field_dict["system_host_cluster"] = system_host_cluster
        if system_apm_cluster is not UNSET:
            field_dict["system_apm_cluster"] = system_apm_cluster
        if default_support_product is not UNSET:
            field_dict["default_support_product"] = default_support_product
        if default_s3_product is not UNSET:
            field_dict["default_s3_product"] = default_s3_product
        if default_assistant_product is not UNSET:
            field_dict["default_assistant_product"] = default_assistant_product
        if default_loadbalancer_product is not UNSET:
            field_dict["default_loadbalancer_product"] = default_loadbalancer_product
        if default_k8s_volume_product is not UNSET:
            field_dict["default_k8s_volume_product"] = default_k8s_volume_product
        if default_internal_dns_zone_product is not UNSET:
            field_dict["default_internal_dns_zone_product"] = default_internal_dns_zone_product
        if default_external_dns_zone_product is not UNSET:
            field_dict["default_external_dns_zone_product"] = default_external_dns_zone_product
        if system_domain_registrar is not UNSET:
            field_dict["system_domain_registrar"] = system_domain_registrar
        if default_s3_bucket_cluster is not UNSET:
            field_dict["default_s3_bucket_cluster"] = default_s3_bucket_cluster
        if system_default_pop is not UNSET:
            field_dict["system_default_pop"] = system_default_pop
        if k8s_cluster_backup_s3_cluster is not UNSET:
            field_dict["k8s_cluster_backup_s3_cluster"] = k8s_cluster_backup_s3_cluster
        if default_k8s_cluster_dns_zone is not UNSET:
            field_dict["default_k8s_cluster_dns_zone"] = default_k8s_cluster_dns_zone
        if system_name is not UNSET:
            field_dict["SYSTEM_NAME"] = system_name
        if system_frontend_base_url is not UNSET:
            field_dict["SYSTEM_FRONTEND_BASE_URL"] = system_frontend_base_url
        if platform_dns_zone is not UNSET:
            field_dict["platform_dns_zone"] = platform_dns_zone
        if global_debug_mode is not UNSET:
            field_dict["global_debug_mode"] = global_debug_mode
        if system_reconciliation_interval_seconds is not UNSET:
            field_dict["SYSTEM_RECONCILIATION_INTERVAL_SECONDS"] = system_reconciliation_interval_seconds
        if system_discovery_interval_seconds is not UNSET:
            field_dict["SYSTEM_DISCOVERY_INTERVAL_SECONDS"] = system_discovery_interval_seconds
        if discovery_enabled is not UNSET:
            field_dict["DISCOVERY_ENABLED"] = discovery_enabled
        if reconciliation_enabled is not UNSET:
            field_dict["RECONCILIATION_ENABLED"] = reconciliation_enabled

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.system_owner_organization, Unset):
            files.append(
                ("system_owner_organization", (None, str(self.system_owner_organization).encode(), "text/plain"))
            )

        if not isinstance(self.system_host_cluster, Unset):
            files.append(("system_host_cluster", (None, str(self.system_host_cluster).encode(), "text/plain")))

        if not isinstance(self.system_apm_cluster, Unset):
            files.append(("system_apm_cluster", (None, str(self.system_apm_cluster).encode(), "text/plain")))

        if not isinstance(self.default_support_product, Unset):
            files.append(("default_support_product", (None, str(self.default_support_product).encode(), "text/plain")))

        if not isinstance(self.default_s3_product, Unset):
            files.append(("default_s3_product", (None, str(self.default_s3_product).encode(), "text/plain")))

        if not isinstance(self.default_assistant_product, Unset):
            files.append(
                ("default_assistant_product", (None, str(self.default_assistant_product).encode(), "text/plain"))
            )

        if not isinstance(self.default_loadbalancer_product, Unset):
            files.append(
                ("default_loadbalancer_product", (None, str(self.default_loadbalancer_product).encode(), "text/plain"))
            )

        if not isinstance(self.default_k8s_volume_product, Unset):
            files.append(
                ("default_k8s_volume_product", (None, str(self.default_k8s_volume_product).encode(), "text/plain"))
            )

        if not isinstance(self.default_internal_dns_zone_product, Unset):
            files.append(
                (
                    "default_internal_dns_zone_product",
                    (None, str(self.default_internal_dns_zone_product).encode(), "text/plain"),
                )
            )

        if not isinstance(self.default_external_dns_zone_product, Unset):
            files.append(
                (
                    "default_external_dns_zone_product",
                    (None, str(self.default_external_dns_zone_product).encode(), "text/plain"),
                )
            )

        if not isinstance(self.system_domain_registrar, Unset):
            files.append(("system_domain_registrar", (None, str(self.system_domain_registrar).encode(), "text/plain")))

        if not isinstance(self.default_s3_bucket_cluster, Unset):
            files.append(
                ("default_s3_bucket_cluster", (None, str(self.default_s3_bucket_cluster).encode(), "text/plain"))
            )

        if not isinstance(self.system_default_pop, Unset):
            files.append(("system_default_pop", (None, str(self.system_default_pop).encode(), "text/plain")))

        if not isinstance(self.k8s_cluster_backup_s3_cluster, Unset):
            files.append(
                (
                    "k8s_cluster_backup_s3_cluster",
                    (None, str(self.k8s_cluster_backup_s3_cluster).encode(), "text/plain"),
                )
            )

        if not isinstance(self.default_k8s_cluster_dns_zone, Unset):
            files.append(
                ("default_k8s_cluster_dns_zone", (None, str(self.default_k8s_cluster_dns_zone).encode(), "text/plain"))
            )

        if not isinstance(self.system_name, Unset):
            files.append(("SYSTEM_NAME", (None, str(self.system_name).encode(), "text/plain")))

        if not isinstance(self.system_frontend_base_url, Unset):
            files.append(
                ("SYSTEM_FRONTEND_BASE_URL", (None, str(self.system_frontend_base_url).encode(), "text/plain"))
            )

        if not isinstance(self.platform_dns_zone, Unset):
            files.append(("platform_dns_zone", (None, str(self.platform_dns_zone).encode(), "text/plain")))

        if not isinstance(self.global_debug_mode, Unset):
            files.append(("global_debug_mode", (None, str(self.global_debug_mode).encode(), "text/plain")))

        if not isinstance(self.system_reconciliation_interval_seconds, Unset):
            files.append(
                (
                    "SYSTEM_RECONCILIATION_INTERVAL_SECONDS",
                    (None, str(self.system_reconciliation_interval_seconds).encode(), "text/plain"),
                )
            )

        if not isinstance(self.system_discovery_interval_seconds, Unset):
            files.append(
                (
                    "SYSTEM_DISCOVERY_INTERVAL_SECONDS",
                    (None, str(self.system_discovery_interval_seconds).encode(), "text/plain"),
                )
            )

        if not isinstance(self.discovery_enabled, Unset):
            files.append(("DISCOVERY_ENABLED", (None, str(self.discovery_enabled).encode(), "text/plain")))

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("RECONCILIATION_ENABLED", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system_owner_organization = d.pop("system_owner_organization", UNSET)

        system_host_cluster = d.pop("system_host_cluster", UNSET)

        system_apm_cluster = d.pop("system_apm_cluster", UNSET)

        default_support_product = d.pop("default_support_product", UNSET)

        default_s3_product = d.pop("default_s3_product", UNSET)

        default_assistant_product = d.pop("default_assistant_product", UNSET)

        default_loadbalancer_product = d.pop("default_loadbalancer_product", UNSET)

        default_k8s_volume_product = d.pop("default_k8s_volume_product", UNSET)

        default_internal_dns_zone_product = d.pop("default_internal_dns_zone_product", UNSET)

        default_external_dns_zone_product = d.pop("default_external_dns_zone_product", UNSET)

        system_domain_registrar = d.pop("system_domain_registrar", UNSET)

        default_s3_bucket_cluster = d.pop("default_s3_bucket_cluster", UNSET)

        system_default_pop = d.pop("system_default_pop", UNSET)

        k8s_cluster_backup_s3_cluster = d.pop("k8s_cluster_backup_s3_cluster", UNSET)

        default_k8s_cluster_dns_zone = d.pop("default_k8s_cluster_dns_zone", UNSET)

        system_name = d.pop("SYSTEM_NAME", UNSET)

        system_frontend_base_url = d.pop("SYSTEM_FRONTEND_BASE_URL", UNSET)

        platform_dns_zone = d.pop("platform_dns_zone", UNSET)

        global_debug_mode = d.pop("global_debug_mode", UNSET)

        system_reconciliation_interval_seconds = d.pop("SYSTEM_RECONCILIATION_INTERVAL_SECONDS", UNSET)

        system_discovery_interval_seconds = d.pop("SYSTEM_DISCOVERY_INTERVAL_SECONDS", UNSET)

        discovery_enabled = d.pop("DISCOVERY_ENABLED", UNSET)

        reconciliation_enabled = d.pop("RECONCILIATION_ENABLED", UNSET)

        patched_system_config_update_request_request = cls(
            system_owner_organization=system_owner_organization,
            system_host_cluster=system_host_cluster,
            system_apm_cluster=system_apm_cluster,
            default_support_product=default_support_product,
            default_s3_product=default_s3_product,
            default_assistant_product=default_assistant_product,
            default_loadbalancer_product=default_loadbalancer_product,
            default_k8s_volume_product=default_k8s_volume_product,
            default_internal_dns_zone_product=default_internal_dns_zone_product,
            default_external_dns_zone_product=default_external_dns_zone_product,
            system_domain_registrar=system_domain_registrar,
            default_s3_bucket_cluster=default_s3_bucket_cluster,
            system_default_pop=system_default_pop,
            k8s_cluster_backup_s3_cluster=k8s_cluster_backup_s3_cluster,
            default_k8s_cluster_dns_zone=default_k8s_cluster_dns_zone,
            system_name=system_name,
            system_frontend_base_url=system_frontend_base_url,
            platform_dns_zone=platform_dns_zone,
            global_debug_mode=global_debug_mode,
            system_reconciliation_interval_seconds=system_reconciliation_interval_seconds,
            system_discovery_interval_seconds=system_discovery_interval_seconds,
            discovery_enabled=discovery_enabled,
            reconciliation_enabled=reconciliation_enabled,
        )

        patched_system_config_update_request_request.additional_properties = d
        return patched_system_config_update_request_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
