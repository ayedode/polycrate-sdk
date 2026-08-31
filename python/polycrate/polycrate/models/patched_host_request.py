from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.host_kind_enum import HostKindEnum, check_host_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.role_28f_enum import Role28FEnum, check_role_28f_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedHostRequest")


@_attrs_define
class PatchedHostRequest:
    """Basis-Serializer für alle ManagedObject Detail-Endpoints.

    Enthält alle generischen Felder eines ManagedObjects.
    Subclasses erweitern diese Liste mit model-spezifischen Feldern.

    Inkludiert:
    - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
    - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
    - organization/workspace als generische ManagedObject-Referenzen (mit URL)
    - created: Kombifeld (created_at, created_at_humanized, created_by)
    - url: Absolute URL zum Object (via get_absolute_url())

    Usage:
        class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
            class Meta(ManagedObjectDetailSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

        Attributes:
            name (str | Unset): Object name (must be a slug)
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (ProviderEnum | Unset): * `loopback` - Loopback
                * `hetzner_cloud` - HETZNER Cloud
                * `hetzner_robot` - HETZNER Robot
                * `bare_metal` - Bare-Metal
                * `powerdns` - PowerDNS
                * `cloudflare` - Cloudflare
                * `rook-ceph` - Rook Ceph
                * `polycrate` - Polycrate
                * `kubernetes` - Kubernetes
                * `helm` - Helm
                * `generic` - Generic
                * `victorialogs` - VictoriaLogs
                * `system` - System
            provider_reference (None | str | Unset):
            reconciliation_enabled (bool | Unset):
            platform_service (bool | Unset):
            kind (HostKindEnum | Unset): * `vm` - Virtual Machine
                * `bare_metal` - Bare-Metal Machine
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            created_by_component (BlankEnum | CreatedByComponentEnum | None | Unset): Component that created this object:
                cli, operator, or api.

                * `cli` - CLI
                * `operator` - Operator
                * `api` - API
            hostname (str | Unset):
            alias (None | str | Unset):
            role (BlankEnum | Role28FEnum | Unset): Host role (e.g. k8s-worker). Spec: polycrate spec inspect 729.

                * `k8s-worker` - Kubernetes Worker
                * `k8s-controlplane` - Kubernetes Controlplane
                * `generic` - Generic
            active (bool | Unset):
            default_ipv4 (None | str | Unset):
            default_ipv6 (None | str | Unset):
            resource_cpu_type (None | str | Unset):
            resource_cpu_cores (int | None | Unset):
            resource_cpu_architecture (None | str | Unset):
            resource_memory (int | None | Unset):
            resource_disk (int | None | Unset):
            provider_location (None | str | Unset):
            provider_image (None | str | Unset):
            provider_image_os_flavor (None | str | Unset):
            provider_image_os_version (None | str | Unset):
            provider_image_os_architecture (None | str | Unset):
            provider_type (None | str | Unset):
            provider_account_id (None | Unset | UUID):
            description (None | str | Unset):
            credential (None | Unset | UUID):
            ssh_keys_id (None | Unset | UUID):
            k8s_cluster (None | Unset | UUID):
            product_id (None | Unset | UUID):
    """

    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: HostKindEnum | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    hostname: str | Unset = UNSET
    alias: None | str | Unset = UNSET
    role: BlankEnum | Role28FEnum | Unset = UNSET
    active: bool | Unset = UNSET
    default_ipv4: None | str | Unset = UNSET
    default_ipv6: None | str | Unset = UNSET
    resource_cpu_type: None | str | Unset = UNSET
    resource_cpu_cores: int | None | Unset = UNSET
    resource_cpu_architecture: None | str | Unset = UNSET
    resource_memory: int | None | Unset = UNSET
    resource_disk: int | None | Unset = UNSET
    provider_location: None | str | Unset = UNSET
    provider_image: None | str | Unset = UNSET
    provider_image_os_flavor: None | str | Unset = UNSET
    provider_image_os_version: None | str | Unset = UNSET
    provider_image_os_architecture: None | str | Unset = UNSET
    provider_type: None | str | Unset = UNSET
    provider_account_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    ssh_keys_id: None | Unset | UUID = UNSET
    k8s_cluster: None | Unset | UUID = UNSET
    product_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        debug_mode = self.debug_mode

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        provider_reference: None | str | Unset
        if isinstance(self.provider_reference, Unset):
            provider_reference = UNSET
        else:
            provider_reference = self.provider_reference

        reconciliation_enabled = self.reconciliation_enabled

        platform_service = self.platform_service

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        tolerations = self.tolerations

        archived = self.archived

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        archived_reason: None | str | Unset
        if isinstance(self.archived_reason, Unset):
            archived_reason = UNSET
        else:
            archived_reason = self.archived_reason

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        target_availability: None | str | Unset
        if isinstance(self.target_availability, Unset):
            target_availability = UNSET
        else:
            target_availability = self.target_availability

        slo_target: None | str | Unset
        if isinstance(self.slo_target, Unset):
            slo_target = UNSET
        else:
            slo_target = self.slo_target

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_availability = self.sla_availability

        created_by_component: None | str | Unset
        if isinstance(self.created_by_component, Unset):
            created_by_component = UNSET
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        else:
            created_by_component = self.created_by_component

        hostname = self.hostname

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        role: str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, str):
            role = self.role
        else:
            role = self.role

        active = self.active

        default_ipv4: None | str | Unset
        if isinstance(self.default_ipv4, Unset):
            default_ipv4 = UNSET
        else:
            default_ipv4 = self.default_ipv4

        default_ipv6: None | str | Unset
        if isinstance(self.default_ipv6, Unset):
            default_ipv6 = UNSET
        else:
            default_ipv6 = self.default_ipv6

        resource_cpu_type: None | str | Unset
        if isinstance(self.resource_cpu_type, Unset):
            resource_cpu_type = UNSET
        else:
            resource_cpu_type = self.resource_cpu_type

        resource_cpu_cores: int | None | Unset
        if isinstance(self.resource_cpu_cores, Unset):
            resource_cpu_cores = UNSET
        else:
            resource_cpu_cores = self.resource_cpu_cores

        resource_cpu_architecture: None | str | Unset
        if isinstance(self.resource_cpu_architecture, Unset):
            resource_cpu_architecture = UNSET
        else:
            resource_cpu_architecture = self.resource_cpu_architecture

        resource_memory: int | None | Unset
        if isinstance(self.resource_memory, Unset):
            resource_memory = UNSET
        else:
            resource_memory = self.resource_memory

        resource_disk: int | None | Unset
        if isinstance(self.resource_disk, Unset):
            resource_disk = UNSET
        else:
            resource_disk = self.resource_disk

        provider_location: None | str | Unset
        if isinstance(self.provider_location, Unset):
            provider_location = UNSET
        else:
            provider_location = self.provider_location

        provider_image: None | str | Unset
        if isinstance(self.provider_image, Unset):
            provider_image = UNSET
        else:
            provider_image = self.provider_image

        provider_image_os_flavor: None | str | Unset
        if isinstance(self.provider_image_os_flavor, Unset):
            provider_image_os_flavor = UNSET
        else:
            provider_image_os_flavor = self.provider_image_os_flavor

        provider_image_os_version: None | str | Unset
        if isinstance(self.provider_image_os_version, Unset):
            provider_image_os_version = UNSET
        else:
            provider_image_os_version = self.provider_image_os_version

        provider_image_os_architecture: None | str | Unset
        if isinstance(self.provider_image_os_architecture, Unset):
            provider_image_os_architecture = UNSET
        else:
            provider_image_os_architecture = self.provider_image_os_architecture

        provider_type: None | str | Unset
        if isinstance(self.provider_type, Unset):
            provider_type = UNSET
        else:
            provider_type = self.provider_type

        provider_account_id: None | str | Unset
        if isinstance(self.provider_account_id, Unset):
            provider_account_id = UNSET
        elif isinstance(self.provider_account_id, UUID):
            provider_account_id = str(self.provider_account_id)
        else:
            provider_account_id = self.provider_account_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        ssh_keys_id: None | str | Unset
        if isinstance(self.ssh_keys_id, Unset):
            ssh_keys_id = UNSET
        elif isinstance(self.ssh_keys_id, UUID):
            ssh_keys_id = str(self.ssh_keys_id)
        else:
            ssh_keys_id = self.ssh_keys_id

        k8s_cluster: None | str | Unset
        if isinstance(self.k8s_cluster, Unset):
            k8s_cluster = UNSET
        elif isinstance(self.k8s_cluster, UUID):
            k8s_cluster = str(self.k8s_cluster)
        else:
            k8s_cluster = self.k8s_cluster

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        elif isinstance(self.product_id, UUID):
            product_id = str(self.product_id)
        else:
            product_id = self.product_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_reference is not UNSET:
            field_dict["provider_reference"] = provider_reference
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if created_by_component is not UNSET:
            field_dict["created_by_component"] = created_by_component
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if alias is not UNSET:
            field_dict["alias"] = alias
        if role is not UNSET:
            field_dict["role"] = role
        if active is not UNSET:
            field_dict["active"] = active
        if default_ipv4 is not UNSET:
            field_dict["default_ipv4"] = default_ipv4
        if default_ipv6 is not UNSET:
            field_dict["default_ipv6"] = default_ipv6
        if resource_cpu_type is not UNSET:
            field_dict["resource_cpu_type"] = resource_cpu_type
        if resource_cpu_cores is not UNSET:
            field_dict["resource_cpu_cores"] = resource_cpu_cores
        if resource_cpu_architecture is not UNSET:
            field_dict["resource_cpu_architecture"] = resource_cpu_architecture
        if resource_memory is not UNSET:
            field_dict["resource_memory"] = resource_memory
        if resource_disk is not UNSET:
            field_dict["resource_disk"] = resource_disk
        if provider_location is not UNSET:
            field_dict["provider_location"] = provider_location
        if provider_image is not UNSET:
            field_dict["provider_image"] = provider_image
        if provider_image_os_flavor is not UNSET:
            field_dict["provider_image_os_flavor"] = provider_image_os_flavor
        if provider_image_os_version is not UNSET:
            field_dict["provider_image_os_version"] = provider_image_os_version
        if provider_image_os_architecture is not UNSET:
            field_dict["provider_image_os_architecture"] = provider_image_os_architecture
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if provider_account_id is not UNSET:
            field_dict["provider_account_id"] = provider_account_id
        if description is not UNSET:
            field_dict["description"] = description
        if credential is not UNSET:
            field_dict["credential"] = credential
        if ssh_keys_id is not UNSET:
            field_dict["ssh_keys_id"] = ssh_keys_id
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.debug_mode, Unset):
            files.append(("debug_mode", (None, str(self.debug_mode).encode(), "text/plain")))

        if not isinstance(self.provider, Unset):
            files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        if not isinstance(self.provider_reference, Unset):
            if isinstance(self.provider_reference, str):
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))
            else:
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("reconciliation_enabled", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.tolerations, Unset):
            files.append(("tolerations", (None, str(self.tolerations).encode(), "text/plain")))

        if not isinstance(self.archived, Unset):
            files.append(("archived", (None, str(self.archived).encode(), "text/plain")))

        if not isinstance(self.archived_at, Unset):
            if isinstance(self.archived_at, datetime.datetime):
                files.append(("archived_at", (None, self.archived_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("archived_at", (None, str(self.archived_at).encode(), "text/plain")))

        if not isinstance(self.archived_reason, Unset):
            if isinstance(self.archived_reason, str):
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))
            else:
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))

        if not isinstance(self.criticality, Unset):
            if isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            else:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))

        if not isinstance(self.target_availability, Unset):
            if isinstance(self.target_availability, str):
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))
            else:
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))

        if not isinstance(self.slo_target, Unset):
            if isinstance(self.slo_target, str):
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))
            else:
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))

        if not isinstance(self.slo_availability, Unset):
            files.append(("slo_availability", (None, str(self.slo_availability).encode(), "text/plain")))

        if not isinstance(self.sla_target, Unset):
            if isinstance(self.sla_target, str):
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))
            else:
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))

        if not isinstance(self.sla_availability, Unset):
            files.append(("sla_availability", (None, str(self.sla_availability).encode(), "text/plain")))

        if not isinstance(self.created_by_component, Unset):
            if isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            elif isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            else:
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))

        if not isinstance(self.hostname, Unset):
            files.append(("hostname", (None, str(self.hostname).encode(), "text/plain")))

        if not isinstance(self.alias, Unset):
            if isinstance(self.alias, str):
                files.append(("alias", (None, str(self.alias).encode(), "text/plain")))
            else:
                files.append(("alias", (None, str(self.alias).encode(), "text/plain")))

        if not isinstance(self.role, Unset):
            if isinstance(self.role, str):
                files.append(("role", (None, str(self.role).encode(), "text/plain")))
            else:
                files.append(("role", (None, str(self.role).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.default_ipv4, Unset):
            if isinstance(self.default_ipv4, str):
                files.append(("default_ipv4", (None, str(self.default_ipv4).encode(), "text/plain")))
            else:
                files.append(("default_ipv4", (None, str(self.default_ipv4).encode(), "text/plain")))

        if not isinstance(self.default_ipv6, Unset):
            if isinstance(self.default_ipv6, str):
                files.append(("default_ipv6", (None, str(self.default_ipv6).encode(), "text/plain")))
            else:
                files.append(("default_ipv6", (None, str(self.default_ipv6).encode(), "text/plain")))

        if not isinstance(self.resource_cpu_type, Unset):
            if isinstance(self.resource_cpu_type, str):
                files.append(("resource_cpu_type", (None, str(self.resource_cpu_type).encode(), "text/plain")))
            else:
                files.append(("resource_cpu_type", (None, str(self.resource_cpu_type).encode(), "text/plain")))

        if not isinstance(self.resource_cpu_cores, Unset):
            if isinstance(self.resource_cpu_cores, int):
                files.append(("resource_cpu_cores", (None, str(self.resource_cpu_cores).encode(), "text/plain")))
            else:
                files.append(("resource_cpu_cores", (None, str(self.resource_cpu_cores).encode(), "text/plain")))

        if not isinstance(self.resource_cpu_architecture, Unset):
            if isinstance(self.resource_cpu_architecture, str):
                files.append(
                    ("resource_cpu_architecture", (None, str(self.resource_cpu_architecture).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("resource_cpu_architecture", (None, str(self.resource_cpu_architecture).encode(), "text/plain"))
                )

        if not isinstance(self.resource_memory, Unset):
            if isinstance(self.resource_memory, int):
                files.append(("resource_memory", (None, str(self.resource_memory).encode(), "text/plain")))
            else:
                files.append(("resource_memory", (None, str(self.resource_memory).encode(), "text/plain")))

        if not isinstance(self.resource_disk, Unset):
            if isinstance(self.resource_disk, int):
                files.append(("resource_disk", (None, str(self.resource_disk).encode(), "text/plain")))
            else:
                files.append(("resource_disk", (None, str(self.resource_disk).encode(), "text/plain")))

        if not isinstance(self.provider_location, Unset):
            if isinstance(self.provider_location, str):
                files.append(("provider_location", (None, str(self.provider_location).encode(), "text/plain")))
            else:
                files.append(("provider_location", (None, str(self.provider_location).encode(), "text/plain")))

        if not isinstance(self.provider_image, Unset):
            if isinstance(self.provider_image, str):
                files.append(("provider_image", (None, str(self.provider_image).encode(), "text/plain")))
            else:
                files.append(("provider_image", (None, str(self.provider_image).encode(), "text/plain")))

        if not isinstance(self.provider_image_os_flavor, Unset):
            if isinstance(self.provider_image_os_flavor, str):
                files.append(
                    ("provider_image_os_flavor", (None, str(self.provider_image_os_flavor).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("provider_image_os_flavor", (None, str(self.provider_image_os_flavor).encode(), "text/plain"))
                )

        if not isinstance(self.provider_image_os_version, Unset):
            if isinstance(self.provider_image_os_version, str):
                files.append(
                    ("provider_image_os_version", (None, str(self.provider_image_os_version).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("provider_image_os_version", (None, str(self.provider_image_os_version).encode(), "text/plain"))
                )

        if not isinstance(self.provider_image_os_architecture, Unset):
            if isinstance(self.provider_image_os_architecture, str):
                files.append(
                    (
                        "provider_image_os_architecture",
                        (None, str(self.provider_image_os_architecture).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "provider_image_os_architecture",
                        (None, str(self.provider_image_os_architecture).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.provider_type, Unset):
            if isinstance(self.provider_type, str):
                files.append(("provider_type", (None, str(self.provider_type).encode(), "text/plain")))
            else:
                files.append(("provider_type", (None, str(self.provider_type).encode(), "text/plain")))

        if not isinstance(self.provider_account_id, Unset):
            if isinstance(self.provider_account_id, UUID):
                files.append(("provider_account_id", (None, str(self.provider_account_id), "text/plain")))
            else:
                files.append(("provider_account_id", (None, str(self.provider_account_id).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.credential, Unset):
            if isinstance(self.credential, UUID):
                files.append(("credential", (None, str(self.credential), "text/plain")))
            else:
                files.append(("credential", (None, str(self.credential).encode(), "text/plain")))

        if not isinstance(self.ssh_keys_id, Unset):
            if isinstance(self.ssh_keys_id, UUID):
                files.append(("ssh_keys_id", (None, str(self.ssh_keys_id), "text/plain")))
            else:
                files.append(("ssh_keys_id", (None, str(self.ssh_keys_id).encode(), "text/plain")))

        if not isinstance(self.k8s_cluster, Unset):
            if isinstance(self.k8s_cluster, UUID):
                files.append(("k8s_cluster", (None, str(self.k8s_cluster), "text/plain")))
            else:
                files.append(("k8s_cluster", (None, str(self.k8s_cluster).encode(), "text/plain")))

        if not isinstance(self.product_id, Unset):
            if isinstance(self.product_id, UUID):
                files.append(("product_id", (None, str(self.product_id), "text/plain")))
            else:
                files.append(("product_id", (None, str(self.product_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        debug_mode = d.pop("debug_mode", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderEnum | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_enum(_provider)

        def _parse_provider_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference", UNSET))

        reconciliation_enabled = d.pop("reconciliation_enabled", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: HostKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_host_kind_enum(_kind)

        tolerations = d.pop("tolerations", UNSET)

        archived = d.pop("archived", UNSET)

        def _parse_archived_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_archived_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archived_reason = _parse_archived_reason(d.pop("archived_reason", UNSET))

        def _parse_criticality(data: object) -> BlankEnum | CriticalityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_0 = check_criticality_enum(data)

                return criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_blank_enum(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CriticalityEnum | None | Unset, data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_target_availability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_availability = _parse_target_availability(d.pop("target_availability", UNSET))

        def _parse_slo_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slo_target = _parse_slo_target(d.pop("slo_target", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

        def _parse_created_by_component(data: object) -> BlankEnum | CreatedByComponentEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_0 = check_created_by_component_enum(data)

                return created_by_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_1 = check_blank_enum(data)

                return created_by_component_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CreatedByComponentEnum | None | Unset, data)

        created_by_component = _parse_created_by_component(d.pop("created_by_component", UNSET))

        hostname = d.pop("hostname", UNSET)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_role(data: object) -> BlankEnum | Role28FEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = check_role_28f_enum(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_1 = check_blank_enum(data)

            return role_type_1

        role = _parse_role(d.pop("role", UNSET))

        active = d.pop("active", UNSET)

        def _parse_default_ipv4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_ipv4 = _parse_default_ipv4(d.pop("default_ipv4", UNSET))

        def _parse_default_ipv6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_ipv6 = _parse_default_ipv6(d.pop("default_ipv6", UNSET))

        def _parse_resource_cpu_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_cpu_type = _parse_resource_cpu_type(d.pop("resource_cpu_type", UNSET))

        def _parse_resource_cpu_cores(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resource_cpu_cores = _parse_resource_cpu_cores(d.pop("resource_cpu_cores", UNSET))

        def _parse_resource_cpu_architecture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_cpu_architecture = _parse_resource_cpu_architecture(d.pop("resource_cpu_architecture", UNSET))

        def _parse_resource_memory(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resource_memory = _parse_resource_memory(d.pop("resource_memory", UNSET))

        def _parse_resource_disk(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resource_disk = _parse_resource_disk(d.pop("resource_disk", UNSET))

        def _parse_provider_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_location = _parse_provider_location(d.pop("provider_location", UNSET))

        def _parse_provider_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_image = _parse_provider_image(d.pop("provider_image", UNSET))

        def _parse_provider_image_os_flavor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_image_os_flavor = _parse_provider_image_os_flavor(d.pop("provider_image_os_flavor", UNSET))

        def _parse_provider_image_os_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_image_os_version = _parse_provider_image_os_version(d.pop("provider_image_os_version", UNSET))

        def _parse_provider_image_os_architecture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_image_os_architecture = _parse_provider_image_os_architecture(
            d.pop("provider_image_os_architecture", UNSET)
        )

        def _parse_provider_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_type = _parse_provider_type(d.pop("provider_type", UNSET))

        def _parse_provider_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_account_id_type_0 = UUID(data)

                return provider_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        provider_account_id = _parse_provider_account_id(d.pop("provider_account_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        def _parse_ssh_keys_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ssh_keys_id_type_0 = UUID(data)

                return ssh_keys_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ssh_keys_id = _parse_ssh_keys_id(d.pop("ssh_keys_id", UNSET))

        def _parse_k8s_cluster(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                k8s_cluster_type_0 = UUID(data)

                return k8s_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        k8s_cluster = _parse_k8s_cluster(d.pop("k8s_cluster", UNSET))

        def _parse_product_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_id_type_0 = UUID(data)

                return product_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        patched_host_request = cls(
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            reconciliation_enabled=reconciliation_enabled,
            platform_service=platform_service,
            kind=kind,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            created_by_component=created_by_component,
            hostname=hostname,
            alias=alias,
            role=role,
            active=active,
            default_ipv4=default_ipv4,
            default_ipv6=default_ipv6,
            resource_cpu_type=resource_cpu_type,
            resource_cpu_cores=resource_cpu_cores,
            resource_cpu_architecture=resource_cpu_architecture,
            resource_memory=resource_memory,
            resource_disk=resource_disk,
            provider_location=provider_location,
            provider_image=provider_image,
            provider_image_os_flavor=provider_image_os_flavor,
            provider_image_os_version=provider_image_os_version,
            provider_image_os_architecture=provider_image_os_architecture,
            provider_type=provider_type,
            provider_account_id=provider_account_id,
            description=description,
            credential=credential,
            ssh_keys_id=ssh_keys_id,
            k8s_cluster=k8s_cluster,
            product_id=product_id,
        )

        patched_host_request.additional_properties = d
        return patched_host_request

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
