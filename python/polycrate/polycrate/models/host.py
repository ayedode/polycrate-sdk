from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.bootstrap_status_enum import BootstrapStatusEnum, check_bootstrap_status_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.host_kind_enum import HostKindEnum, check_host_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.role_28f_enum import Role28FEnum, check_role_28f_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_simple import CredentialSimple
    from ..models.host_created import HostCreated
    from ..models.host_deleted_by_user_type_0 import HostDeletedByUserType0
    from ..models.host_last_action_run_type_0 import HostLastActionRunType0
    from ..models.host_organization_type_0 import HostOrganizationType0
    from ..models.host_workspace_type_0 import HostWorkspaceType0
    from ..models.product_simple import ProductSimple
    from ..models.provider_account_simple import ProviderAccountSimple


T = TypeVar("T", bound="Host")


@_attrs_define
class Host:
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
            id (UUID):
            name (str): Object name (must be a slug)
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (HostDeletedByUserType0 | None):
            provider_id (None | str):
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            last_state_change (datetime.datetime | None):
            reconciliation_running (bool):
            reconciliation_task_id (None | str):
            reconciliation_task_meta (Any): Task metadata for reconciliation progress tracking (e.g., step, progress,
                started_at)
            last_reconciliation (datetime.datetime | None):
            discovery_enabled (bool):
            discovery_running (bool):
            discovery_task_id (None | str):
            discovery_task_meta (Any): Task metadata for discovery progress tracking
            last_discovery (datetime.datetime | None):
            repair_running (bool):
            repair_task_id (None | str):
            repair_task_meta (Any): Task metadata for repair progress tracking
            last_repair (datetime.datetime | None):
            scope (ScopeEnum): * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            effective_criticality (EffectiveCriticalityEnum | None):
            actual_availability (str): Calculated actual availability as yearly average in %
            organization (HostOrganizationType0 | None):
            workspace (HostWorkspaceType0 | None):
            created (HostCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (HostLastActionRunType0 | None): Gibt den letzten ActionRun für das Objekt zurück (für Dashboard
                Footer).

                Unterstützte Relationen:
                - Direkter action_runs Manager (Workspace, Block, Organization)
                - Workspace-FK-Fallback, nur wenn show_last_action_run=True (K8sCluster, K8sApp)

                Spec: polycrate spec inspect 271
            hostname (str):
            bootstrap_status (BootstrapStatusEnum): * `pending` - Pending
                * `provisioning` - Provisioning
                * `ready` - Ready
                * `joining` - Joining
                * `failed` - Failed
                * `deprovisioning` - Deprovisioning
            cloud_init_hash (str): SHA-256 of last applied machine cloud-init payload.
            default_ipv4_rtt (float | None):
            default_ipv4_pl (float | None):
            default_ipv6_rtt (float | None):
            default_ipv6_pl (float | None):
            provider_datacenter (None | str):
            provider_object_id (None | str):
            provider_account (ProviderAccountSimple):
            ssh_keys (CredentialSimple): Simple serializer for embedding Credential in other serializers.
            product (ProductSimple): Compact serializer for embedding Product as FK reference.
            computed_cost (float):
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
            description (None | str | Unset):
            credential (None | Unset | UUID):
            k8s_cluster (None | Unset | UUID):
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: HostDeletedByUserType0 | None
    provider_id: None | str
    state: LastStateEnum
    state_reason: None | str
    last_state: LastStateEnum
    last_state_change: datetime.datetime | None
    reconciliation_running: bool
    reconciliation_task_id: None | str
    reconciliation_task_meta: Any
    last_reconciliation: datetime.datetime | None
    discovery_enabled: bool
    discovery_running: bool
    discovery_task_id: None | str
    discovery_task_meta: Any
    last_discovery: datetime.datetime | None
    repair_running: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    scope: ScopeEnum
    conditions: Any
    effective_criticality: EffectiveCriticalityEnum | None
    actual_availability: str
    organization: HostOrganizationType0 | None
    workspace: HostWorkspaceType0 | None
    created: HostCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: HostLastActionRunType0 | None
    hostname: str
    bootstrap_status: BootstrapStatusEnum
    cloud_init_hash: str
    default_ipv4_rtt: float | None
    default_ipv4_pl: float | None
    default_ipv6_rtt: float | None
    default_ipv6_pl: float | None
    provider_datacenter: None | str
    provider_object_id: None | str
    provider_account: ProviderAccountSimple
    ssh_keys: CredentialSimple
    product: ProductSimple
    computed_cost: float
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
    description: None | str | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    k8s_cluster: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.host_deleted_by_user_type_0 import HostDeletedByUserType0  # noqa: PLC0415
        from ..models.host_last_action_run_type_0 import HostLastActionRunType0  # noqa: PLC0415
        from ..models.host_organization_type_0 import HostOrganizationType0  # noqa: PLC0415
        from ..models.host_workspace_type_0 import HostWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, HostDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        provider_id: None | str
        provider_id = self.provider_id

        state: str = self.state

        state_reason: None | str
        state_reason = self.state_reason

        last_state: str = self.last_state

        last_state_change: None | str
        if isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_running = self.reconciliation_running

        reconciliation_task_id: None | str
        reconciliation_task_id = self.reconciliation_task_id

        reconciliation_task_meta = self.reconciliation_task_meta

        last_reconciliation: None | str
        if isinstance(self.last_reconciliation, datetime.datetime):
            last_reconciliation = self.last_reconciliation.isoformat()
        else:
            last_reconciliation = self.last_reconciliation

        discovery_enabled = self.discovery_enabled

        discovery_running = self.discovery_running

        discovery_task_id: None | str
        discovery_task_id = self.discovery_task_id

        discovery_task_meta = self.discovery_task_meta

        last_discovery: None | str
        if isinstance(self.last_discovery, datetime.datetime):
            last_discovery = self.last_discovery.isoformat()
        else:
            last_discovery = self.last_discovery

        repair_running = self.repair_running

        repair_task_id: None | str
        repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        last_repair: None | str
        if isinstance(self.last_repair, datetime.datetime):
            last_repair = self.last_repair.isoformat()
        else:
            last_repair = self.last_repair

        scope: str = self.scope

        conditions = self.conditions

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        actual_availability = self.actual_availability

        organization: dict[str, Any] | None
        if isinstance(self.organization, HostOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, HostWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, HostLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        hostname = self.hostname

        bootstrap_status: str = self.bootstrap_status

        cloud_init_hash = self.cloud_init_hash

        default_ipv4_rtt: float | None
        default_ipv4_rtt = self.default_ipv4_rtt

        default_ipv4_pl: float | None
        default_ipv4_pl = self.default_ipv4_pl

        default_ipv6_rtt: float | None
        default_ipv6_rtt = self.default_ipv6_rtt

        default_ipv6_pl: float | None
        default_ipv6_pl = self.default_ipv6_pl

        provider_datacenter: None | str
        provider_datacenter = self.provider_datacenter

        provider_object_id: None | str
        provider_object_id = self.provider_object_id

        provider_account = self.provider_account.to_dict()

        ssh_keys = self.ssh_keys.to_dict()

        product = self.product.to_dict()

        computed_cost = self.computed_cost

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

        k8s_cluster: None | str | Unset
        if isinstance(self.k8s_cluster, Unset):
            k8s_cluster = UNSET
        elif isinstance(self.k8s_cluster, UUID):
            k8s_cluster = str(self.k8s_cluster)
        else:
            k8s_cluster = self.k8s_cluster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "deleted_by_user": deleted_by_user,
                "provider_id": provider_id,
                "state": state,
                "state_reason": state_reason,
                "last_state": last_state,
                "last_state_change": last_state_change,
                "reconciliation_running": reconciliation_running,
                "reconciliation_task_id": reconciliation_task_id,
                "reconciliation_task_meta": reconciliation_task_meta,
                "last_reconciliation": last_reconciliation,
                "discovery_enabled": discovery_enabled,
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "scope": scope,
                "conditions": conditions,
                "effective_criticality": effective_criticality,
                "actual_availability": actual_availability,
                "organization": organization,
                "workspace": workspace,
                "created": created,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "last_action_run": last_action_run,
                "hostname": hostname,
                "bootstrap_status": bootstrap_status,
                "cloud_init_hash": cloud_init_hash,
                "default_ipv4_rtt": default_ipv4_rtt,
                "default_ipv4_pl": default_ipv4_pl,
                "default_ipv6_rtt": default_ipv6_rtt,
                "default_ipv6_pl": default_ipv6_pl,
                "provider_datacenter": provider_datacenter,
                "provider_object_id": provider_object_id,
                "provider_account": provider_account,
                "ssh_keys": ssh_keys,
                "product": product,
                "computed_cost": computed_cost,
            }
        )
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
        if description is not UNSET:
            field_dict["description"] = description
        if credential is not UNSET:
            field_dict["credential"] = credential
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_simple import CredentialSimple  # noqa: PLC0415
        from ..models.host_created import HostCreated  # noqa: PLC0415
        from ..models.host_deleted_by_user_type_0 import HostDeletedByUserType0  # noqa: PLC0415
        from ..models.host_last_action_run_type_0 import HostLastActionRunType0  # noqa: PLC0415
        from ..models.host_organization_type_0 import HostOrganizationType0  # noqa: PLC0415
        from ..models.host_workspace_type_0 import HostWorkspaceType0  # noqa: PLC0415
        from ..models.product_simple import ProductSimple  # noqa: PLC0415
        from ..models.provider_account_simple import ProviderAccountSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        is_deleted = d.pop("is_deleted")

        def _parse_deleted_by_user(data: object) -> HostDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = HostDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        def _parse_provider_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        state = check_last_state_enum(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_last_state_enum(d.pop("last_state"))

        def _parse_last_state_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_state_change_type_0 = datetime.datetime.fromisoformat(data)

                return last_state_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_state_change = _parse_last_state_change(d.pop("last_state_change"))

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_reconciliation_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reconciliation_task_id = _parse_reconciliation_task_id(d.pop("reconciliation_task_id"))

        reconciliation_task_meta = d.pop("reconciliation_task_meta")

        def _parse_last_reconciliation(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reconciliation_type_0 = datetime.datetime.fromisoformat(data)

                return last_reconciliation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_reconciliation = _parse_last_reconciliation(d.pop("last_reconciliation"))

        discovery_enabled = d.pop("discovery_enabled")

        discovery_running = d.pop("discovery_running")

        def _parse_discovery_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        discovery_task_id = _parse_discovery_task_id(d.pop("discovery_task_id"))

        discovery_task_meta = d.pop("discovery_task_meta")

        def _parse_last_discovery(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_discovery_type_0 = datetime.datetime.fromisoformat(data)

                return last_discovery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_discovery = _parse_last_discovery(d.pop("last_discovery"))

        repair_running = d.pop("repair_running")

        def _parse_repair_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repair_task_id = _parse_repair_task_id(d.pop("repair_task_id"))

        repair_task_meta = d.pop("repair_task_meta")

        def _parse_last_repair(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_repair_type_0 = datetime.datetime.fromisoformat(data)

                return last_repair_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_repair = _parse_last_repair(d.pop("last_repair"))

        scope = check_scope_enum(d.pop("scope"))

        conditions = d.pop("conditions")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        actual_availability = d.pop("actual_availability")

        def _parse_organization(data: object) -> HostOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = HostOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> HostWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = HostWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = HostCreated.from_dict(d.pop("created"))

        url = d.pop("url")

        icon_url = d.pop("icon_url")

        is_class_icon = d.pop("is_class_icon")

        def _parse_effective_slo_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_slo_target = _parse_effective_slo_target(d.pop("effective_slo_target"))

        def _parse_effective_sla_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_sla_target = _parse_effective_sla_target(d.pop("effective_sla_target"))

        def _parse_last_action_run(data: object) -> HostLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = HostLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        hostname = d.pop("hostname")

        bootstrap_status = check_bootstrap_status_enum(d.pop("bootstrap_status"))

        cloud_init_hash = d.pop("cloud_init_hash")

        def _parse_default_ipv4_rtt(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        default_ipv4_rtt = _parse_default_ipv4_rtt(d.pop("default_ipv4_rtt"))

        def _parse_default_ipv4_pl(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        default_ipv4_pl = _parse_default_ipv4_pl(d.pop("default_ipv4_pl"))

        def _parse_default_ipv6_rtt(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        default_ipv6_rtt = _parse_default_ipv6_rtt(d.pop("default_ipv6_rtt"))

        def _parse_default_ipv6_pl(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        default_ipv6_pl = _parse_default_ipv6_pl(d.pop("default_ipv6_pl"))

        def _parse_provider_datacenter(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_datacenter = _parse_provider_datacenter(d.pop("provider_datacenter"))

        def _parse_provider_object_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_object_id = _parse_provider_object_id(d.pop("provider_object_id"))

        provider_account = ProviderAccountSimple.from_dict(d.pop("provider_account"))

        ssh_keys = CredentialSimple.from_dict(d.pop("ssh_keys"))

        product = ProductSimple.from_dict(d.pop("product"))

        computed_cost = d.pop("computed_cost")

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

        host = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            deleted_by_user=deleted_by_user,
            provider_id=provider_id,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            last_reconciliation=last_reconciliation,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            scope=scope,
            conditions=conditions,
            effective_criticality=effective_criticality,
            actual_availability=actual_availability,
            organization=organization,
            workspace=workspace,
            created=created,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            last_action_run=last_action_run,
            hostname=hostname,
            bootstrap_status=bootstrap_status,
            cloud_init_hash=cloud_init_hash,
            default_ipv4_rtt=default_ipv4_rtt,
            default_ipv4_pl=default_ipv4_pl,
            default_ipv6_rtt=default_ipv6_rtt,
            default_ipv6_pl=default_ipv6_pl,
            provider_datacenter=provider_datacenter,
            provider_object_id=provider_object_id,
            provider_account=provider_account,
            ssh_keys=ssh_keys,
            product=product,
            computed_cost=computed_cost,
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
            description=description,
            credential=credential,
            k8s_cluster=k8s_cluster,
        )

        host.additional_properties = d
        return host

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
